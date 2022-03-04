# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields,models



class  AccountMoveLine(models.Model):
    _inherit = "account.move.line"


    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super()._onchange_product_id()
        if self.product_id and self.partner_id:
            self.product_uom_id = self.partner_id.product_uom_detail_ids.filtered(lambda x : x.product_id.id == self.product_id.id).uom_id.id
        return res

