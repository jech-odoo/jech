# -*- coding: utf-8 -*-

from odoo import models, api, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    narration = fields.Html(string='Terms and Conditions', default='Terms and conditions...')
    reseller_id = fields.Many2one("res.partner", string="Reseller")
    commission_percentage = fields.Float(string="Commission (%)")


    @api.onchange('partner_id')
    def _onchange_partner_id_incoterms(self):
        if self.move_type in ['out_invoice', 'out_refund', 'out_receipt']:
            self.invoice_incoterm_id = self.partner_id.sales_incoterm_id.id or False

        if self.move_type in ['in_invoice', 'in_refund', 'in_receipt']:
            self.invoice_incoterm_id = self.partner_id.purchase_incoterm_id.id or False

