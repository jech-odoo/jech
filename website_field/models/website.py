from odoo import models


class Website(models.Model):

    _inherit = "website"

    city = models.Char("city")