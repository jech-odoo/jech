# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Inventory(models.Model):
    _name = 'product.uom.detail'
    product_id = fields.Many2one('product.product')
    uom_id = fields.Many2one('uom.uom', domain="[('category_id','=',uom_category)]")
    partner_id = fields.Many2one('res.partner')
    uom_category = fields.Many2one(related="product_id.uom_id.category_id")




