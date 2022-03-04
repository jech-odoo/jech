# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    secound_discount = fields.Float(string="2nd disc%")

    @api.depends('price_subtotal', 'secound_discount', 'price_unit')
    def _compute_amount(self):
       res = super()._compute_amount()
       for line in self:
              line.price_subtotal = line.price_subtotal - (line.price_subtotal * line.secound_discount  / 100)
       return res 