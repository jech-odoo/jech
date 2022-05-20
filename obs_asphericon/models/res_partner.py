# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    fax = fields.Char(string="Fax")
    department = fields.Char(string="Department")
    rating = fields.Many2one("vendor.rating", string="Rating")
