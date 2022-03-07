from odoo import models, fields


class SaleApproval(models.Model):
    _inherit = 'sale.order'

    # ------------------------
    #  fields Declaration
    # ------------------------

    zero_stock_approval = fields.Boolean(string='Approval')

