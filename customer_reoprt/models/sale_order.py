
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields,models


class SaleOrder(models.Model):
    # -------------------------
    # Inherite fields
    # -------------------------

    _inherit = 'sale.order'

    # ----------------------------
    #  fields Declaration
    # ---------------------------

   
    enquiry = fields.Integer(string="enquirey")
    mark = fields.Char(string="mark")
