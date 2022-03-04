# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields,models


class ResPartner(models.Model):
    # -------------------------
    # Inherite fields
    # -------------------------

    _inherit = 'res.partner'

    # ----------------------------
    #  fields Declaration
    # ---------------------------

   
    product_uom_detail_ids = fields.One2many(comodel_name='product.uom.detail',inverse_name='partner_id',
                                             string='Product Uom', required=False)
