# -*- coding: utf-8 -*-
import string
from odoo import fields, models, api, _
from odoo.exceptions import Warning


class ProjectWizard(models.TransientModel):
    _name = "project.template.wizard"
    _description = "Create a Project"

    name = fields.Char(string="Name")
    project_id = fields.Many2one("project.project", string="Project")
    allow_forecast = fields.Boolean(
        "Planning", default=True, help="Enable planning tasks on the project."
    )
    allow_timesheets = fields.Boolean(
        "Timesheets", default=True, help="Enable timesheeting on the project."
    )
    allow_billable = fields.Boolean(
        "Billable", help="Invoice your time and material from tasks."
    )
    user_id = fields.Many2one(
        "res.users", string="Assigned to", default=lambda self: self.env.uid
    )
    project_manager_id = fields.Many2one(
        "res.users", string="Project Manager", default=lambda self: self.env.uid
    )

    @api.onchange("project_id")
    def _onchange_project_id(self):
        if not self.project_id:
            return
        self.allow_billable = self.project_id.allow_billable
        self.allow_forecast = self.project_id.allow_forecast
        self.allow_timesheets = self.project_id.allow_timesheets

    def prepare_project_values(self):
        vals = {
            "name": self.name,
            "allow_forecast": self.allow_forecast,
            "allow_timesheets": self.allow_timesheets,
            "allow_billable": self.allow_billable,
            "user_id": self.project_manager_id.id,
        }
        return vals

    def action_create_project_template(self):
        project_vals = self.prepare_project_values()
        # if no Project selected from the list then it will create a new record
        if self.name and self.env["project.project"].search([("name", "=", self.name)]):
            raise Warning(
                _(
                    "This project name is already taken. Please use another name or change the name of the other project(s) first."
                )
            )

        if not self.project_id:
            project = self.env["project.project"].create(project_vals)

        # if Project is selected  then it will copy the selected project to create a new record with default vals
        else:
            project = self.project_id.copy(
                {"name": self.name, "user_id": self.project_manager_id.id}
            )
        # checking if project is created on the fly from the CRM or Sales Order form
        # if yes then link the newly created project to the respected record
        context = dict(self._context)
        active_model, active_id = context.get("active_model"), context.get("active_id")
        if active_id and active_model:
            record = self.env[active_model].browse(active_id)
            if record:
                project.update({"partner_id": record.partner_id.id})
                record.write({"project_ids": [(4, project.id)]})
                if active_model == "sale.order":
                    record.write(
                        {"analytic_account_id": project.analytic_account_id.id}
                    )
                return {"type": "ir.actions.act_window_close"}
        return self.env["ir.actions.act_window"]._for_xml_id(
            "project.open_view_project_all"
        )
