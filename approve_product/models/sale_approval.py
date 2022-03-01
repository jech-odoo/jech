from odoo import models, fields


class SaleApproval(models.Model):
    _inherit = 'sale.order'

    # ----------------------------
    #  fields Declarations
    # ---------------------------

    zero_stock_approval = fields.Boolean(string='Approval')


# def _approval(self):
#     if self.env.uid == self.parent_id.user_id.id:
#         self.zero_stock_approval = True
