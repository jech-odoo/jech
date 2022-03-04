# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # ------------------------
    #  fields Declaration
    # ------------------------

    zero_stock_approval = fields.Boolean(string='Approval')


