
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models,fields,api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('amount_untaxed')
    def _check_total_receivable_sale(self):
        credit_total = self.amount_untaxed + self.partner_id.credit
        if credit_total > self.partner_id.credit_limit:
            raise UserError("total receivable amount exceeds the credit limit")
        