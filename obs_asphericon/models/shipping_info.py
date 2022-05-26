# -*- coding: utf-8 -*-

from odoo import models, fields


class ShippingInfo(models.Model):
    _name = "shipping.info"
    _description = "Shipping Info"

    name = fields.Char(string="Name")
    number = fields.Integer(string="Number")
