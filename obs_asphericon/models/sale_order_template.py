from odoo import fields, models


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    note = fields.Html('Terms and conditions', translate=True, default='The Administrator can set default Terms & Conditions in Sales Settings. Terms set here will show up instead if you select this quotation template.')
