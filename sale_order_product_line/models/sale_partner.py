from odoo import models, api,fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_ordr_id = fields.Many2one('sale.order', string="Customer Order" , domain="[('partner_id', '=',partner_id)]")

