from odoo import fields, models
from random import randint


class ProductTags(models.Model):
    _name = "product.tags"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Tag Name", translate=True)
    color = fields.Integer(string='Color', default=_get_default_color)
