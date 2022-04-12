from odoo import models,fields


class PosOrder(models.Model):
    _inherit = 'pos.order'

    zip_id = fields.Char(related='partner_id.zip')

