from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    invoice_terms = fields.Html(string='Default Terms and Conditions', translate=True)