from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_terms = fields.Html(related='company_id.invoice_terms', string="Terms & Conditions", readonly=False)
