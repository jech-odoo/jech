# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = "project.task"

    project_manager_id = fields.Many2one(
        "res.users", string="Project Manager", related="project_id.user_id"
    )
