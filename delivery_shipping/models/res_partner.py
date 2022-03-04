# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResPartner(models.Model):
    # -------------------------
    # Inherite fields
    # -------------------------

    _inherit = 'res.partner'

    # ----------------------------
    #  fields Declaration
    # ---------------------------

    day_to_delivrer = fields.Integer(string="Days to Deliver")
    