# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields,api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # -------------------------
    #  fields Declaration
    # --------------------------

   
    product_id = fields.Many2many('product.product', compute='_compute_products')

    @api.depends("move_ids_without_package.product_id")
    def _compute_products(self):
        for record in self:
            record.product_id = record.move_ids_without_package.product_id.ids
