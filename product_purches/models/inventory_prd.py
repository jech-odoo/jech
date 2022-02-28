# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Inventory(models.Model):
    _name = 'product.uom.detail'
    product_id = fields.Many2one('product.product')
    uom_id = fields.Many2one('uom.uom', domain="[('category_id','=',uom_category)]")
    partner_id = fields.Many2one('res.partner')
    uom_category = fields.Many2one(related="product_id.uom_id.category_id")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        for line in self:
            if line.order_id.partner_id:
                if line.order_id.partner_id.product_uom_detail_ids:
                    uom_details_ids = line.order_id.partner_id.product_uom_detail_ids
                    for record in uom_details_ids:
                        if line.product_id == record.product_id:
                            line.product_uom = record.uom_id
        return res



