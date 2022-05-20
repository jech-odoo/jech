# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_earlier = fields.Char(compute='_compute_is_earlier')
    shipping_info_id = fields.Many2one(
        "shipping.info", string="Shipping Info", related="sale_id.shipping_info_id", readonly=False, store=1)
    number = fields.Integer(related="shipping_info_id.number", string="Number")

    @api.depends('scheduled_date')
    def _compute_is_earlier(self):
        for pick in self:
            pick.is_earlier = True if pick.scheduled_date > fields.Datetime.now() else False
