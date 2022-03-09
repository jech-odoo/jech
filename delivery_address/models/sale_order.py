# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # ------------------------
    #  fields Declaration
    # ------------------------

    re_seller_id = fields.Many2one('res.partner')
    commission_amount = fields.Float(string="Commission")

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            're_seller_id':self.re_seller_id.id,
            'commission_amount':self.commission_amount,
            })
        print("\n\n RES IS", res)
        return res

