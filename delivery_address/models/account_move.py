# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields,api

class AccountMove(models.Model):
    _inherit = 'account.move'

    # ------------------------
    #  fields Declaration
    # ------------------------
        
    re_seller_id = fields.Many2one('res.partner')
    commission_amount = fields.Float(string="Commission")