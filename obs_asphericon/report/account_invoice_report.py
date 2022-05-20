from odoo import fields, models

class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'
    
    commission_percenatge = fields.Float(string="Commission (%)")
    reseller_id = fields.Many2one('res.partner', 'Reseller')
    
    def _select(self):
        res = super()._select()
        select_str = res + """, move.commission_percentage AS commission_percenatge, move.reseller_id as reseller_id"""
        return select_str