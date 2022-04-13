# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    bom_id = fields.Many2one('mrp.bom')
    # bom_temp_ids=fields.One2many('mrp.bom','product_id')
