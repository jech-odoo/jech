# -*- coding: utf-8 -*-

from odoo import fields, models, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    saleable_quantities = fields.Float('Saleable', compute="_compute_product_saleable_quantities")

    @api.depends('location_id')
    def _compute_product_saleable_quantities(self):
        available_qty = 0.0
        self.saleable_quantities = available_qty
        for quant in self:
            if quant.location_id.is_saleable_quantities:
                product_quants = quant.location_id.quant_ids.filtered(lambda l: l.product_id == quant.product_id)
                if product_quants:
                    for product_quant in product_quants:
                        available_qty = product_quant.available_quantity
                    quant.saleable_quantities = available_qty

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        """
            Override read_group to calculate the sum of the non-stored fields that depend on the user context
        """
        res = super().read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        quants = self.env['stock.quant']
        saleable_quantities = 0.0
        for line in res:
            if '__domain' in line:
                quants = self.search(line['__domain'])
            if 'saleable_quantities' in fields:
                saleable_quantities = sum(quants.mapped('saleable_quantities'))
                line['saleable_quantities'] = saleable_quantities
        return res
