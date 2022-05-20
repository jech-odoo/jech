# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductCategory(models.Model):
    _inherit = 'product.category'
    _rec_name = 'name'
    name = fields.Char('Name', index=True, required=True, translate=True)
    display_name = fields.Char(
        compute='_compute_display_name', index=True, translate=True)
    ignore_sales_price = fields.Boolean(string="Ignore Sales Prices")
    ignore_vendor_pricelists = fields.Boolean(string="Ignore Vendor Pricelists")

    @api.depends('name', 'parent_id.display_name')
    def _compute_display_name(self):
        for category in self:
            if category.parent_id:
                category.display_name = '%s / %s' % (
                    category.parent_id.display_name, category.name)
            else:
                category.display_name = category.name

    def name_get(self):
        result = []
        for category in self:
            if category.parent_id:
                result.append((category.id, '%s / %s' % (
                    category.parent_id.display_name, category.name)))
            else:
                result.append((category.id, category.name))
        return result
