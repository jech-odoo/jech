# -*- coding: utf-8 -*-

from odoo import models, fields


class VendorRating(models.Model):
    _name = "vendor.rating"
    _description = "Vendor Rating"

    name = fields.Char(string="Name")
