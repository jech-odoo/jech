# -*- coding: utf-8 -*-
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
