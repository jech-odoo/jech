from odoo import models, fields, api


class SaleApproval(models.Model):
    _inherit = 'sale.order'

    # ------------------------
    #  fields Declaration
    # ------------------------

    zero_stock_approval = fields.Boolean(string='Approval')


def _approval(self):
    if self.env.uid == self.parent_id.user_id.id:
        self.zero_stock_approval = True
