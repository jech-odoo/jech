# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CRMLead(models.Model):
    _inherit = "crm.lead"

    industry_id = fields.Many2one("res.partner.industry", string="Industry")
    project_ids = fields.Many2many("project.project", string="Projects")

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        self.industry_id = self.partner_id.industry_id or False

    # inherited method to add industry_id during new contact creation from opportunity
    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        res = super()._prepare_customer_values(
            partner_name, is_company=is_company, parent_id=parent_id
        )
        res.update(
            {
                "industry_id": self.industry_id.id,
                "company_id": self.company_id.id,
            }
        )
        return res

    def action_open_projects(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "sale_timesheet.project_timesheet_action_client_timesheet_plan"
        )
        action["domain"] = [("id", "in", self.project_ids.ids)]
        action["context"] = {"create": False}
        return action

    def action_open_create_project(self):
        return {
            "name": "Create a Project",
            "type": "ir.actions.act_window",
            "res_model": "project.template.wizard",
            "target": "new",
            "views": [[False, "form"]],
        }
