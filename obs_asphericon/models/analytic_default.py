# -*- coding: utf-8 -*-

from odoo import models, fields


class AnalyticDefault(models.Model):
    _inherit = "account.analytic.default"

    is_from_product = fields.Boolean(string="Created from product")
