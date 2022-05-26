# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class MRPProdction(models.Model):
    _inherit = "mrp.production"

    analytic_account_id = fields.Many2one(
        "account.analytic.account",
        "Analytic Account",
        copy=True,
        help="Analytic account in which cost and revenue entries will take\
        place for financial management of the manufacturing order.",
        readonly=False,
    )

    date_deadline = fields.Datetime(
        "Deadline",
        copy=False,
        readonly=True,
        compute="_compute_deadline_date",
        help="Informative date allowing to define when the manufacturing order should be processed at the latest to fulfill delivery on time.",
    )

    restrict_partner_id = fields.Many2one("res.partner", string="Owner", copy=False)
    product_tags = fields.Many2many(
        "product.tags", string="Product Tags", related="product_id.tag_ids"
    )
    is_cost_calculated = fields.Boolean(
        string="Cost Calculated", groups="mrp.group_mrp_manager", copy=False
    )
    project_count = fields.Integer(compute="_compute_project_count")

    @api.onchange("product_id", "picking_type_id", "company_id")
    def onchange_product_id(self):
        super().onchange_product_id()
        if self._context.get("default_analytic_id"):
            self.analytic_account_id = self._context.get("default_analytic_id")
        else:
            self.analytic_account_id = (
                self.env["account.analytic.default"]
                .search(
                    [
                        ("product_id", "=", self.product_id.id),
                        ("product_id", "!=", False),
                    ],
                    limit=1,
                )
                .analytic_id.id
            )

    @api.onchange("date_planned_start", "product_id")
    def _onchange_date_planned_start(self):
        if self.date_planned_start and not self.is_planned:
            self.move_raw_ids = [
                (1, m.id, {"date": self.date_planned_start}) for m in self.move_raw_ids
            ]
            self.move_finished_ids = [
                (1, m.id, {"date": self.date_planned_finished})
                for m in self.move_finished_ids
            ]

    def action_view_analytic_account(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "account.analytic.account",
            "res_id": self.analytic_account_id.id,
            "context": {"create": False},
            "name": "Analytic Account",
            "view_mode": "form",
        }

    @api.depends("product_id", "date_planned_start")
    def _compute_deadline_date(self):
        for production in self:
            if not production.origin:
                if production.date_planned_start:
                    production.date_deadline = (
                        production.date_planned_start
                        + timedelta(days=production.product_id.produce_delay)
                    )

    @api.depends("analytic_account_id")
    def _compute_project_count(self):
        Project = self.env["project.project"]
        for production in self:
            production.project_count = Project.search_count(
                [("analytic_account_id", "=", production.analytic_account_id.id)]
            )

    @api.depends(
        "workorder_ids.state", "move_finished_ids", "move_finished_ids.quantity_done"
    )
    def _get_produced_qty(self):
        """Set the owner on the finished product when it's move to the stock
        Returns:
            produced qty of the main product
        """
        produced_qty = super()._get_produced_qty()
        for production in self:
            if production.restrict_partner_id:
                done_moves = production.move_finished_ids.filtered(
                    lambda x: x.state != "cancel"
                    and x.product_id.id == production.product_id.id
                )
                done_moves.write(
                    {"restrict_partner_id": production.restrict_partner_id.id}
                )
                done_moves.move_line_ids.write(
                    {"owner_id": production.restrict_partner_id.id}
                )
        return produced_qty

    def action_assign(self):
        res = super().action_assign()
        moves = self.mapped("move_raw_ids")
        if moves:
            moves[0].move_line_ids.production_id.write(
                {"restrict_partner_id": moves[0].move_line_ids.owner_id.id}
            )
        return res

    def button_unreserve(self):
        unreserve = super().button_unreserve()
        self.restrict_partner_id = False
        return unreserve

    def action_open_projects(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "sale_timesheet.project_timesheet_action_client_timesheet_plan"
        )
        action["domain"] = [("analytic_account_id", "=", self.analytic_account_id.id)]
        action["context"] = {"create": False}
        return action

    def _generate_backorder_productions(self, close_mo=True):
        """
        Inherited to get the backorders created by clicking Create Back order button on mpr.production model
        It will update the res_id of the activity which was originally created for the main manufacturing order to
        the newly created backorder
        """
        current_mo = self
        res = super()._generate_backorder_productions(close_mo=close_mo)
        res.is_cost_calculated = current_mo.is_cost_calculated
        mail_activities = self.env["mail.activity"].search(
            [("res_model", "=", "mrp.production"), ("res_id", "=", current_mo.id)]
        )
        if mail_activities:
            mail_activities.write({"res_id": res.id})
        messages = self.env["mail.message"].search(
            [
                ("message_type", "in", ("comment", "notification")),
                ("model", "=", "mrp.production"),
                ("res_id", "=", current_mo.id),
            ]
        )
        if messages:
            messages.write({"res_id": res.id, "record_name": res.name})
        return res
