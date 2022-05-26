# -*- coding: utf-8 -*-

from odoo import api, models, fields, _


class StockLocation(models.Model):
    _inherit = "stock.location"

    is_saleable_quantities = fields.Boolean(string="Saleable Quantities?")

    @api.onchange("usage")
    def onchange_usage(self):
        if not self.usage == "internal":
            self.is_saleable_quantities = False
