# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QualityAlert(models.Model):
    _inherit = 'quality.alert'

    representative_id = fields.Many2one(
        "res.users", string="Purchase Representative", compute='_compute_representative_id')

    @api.depends('picking_id')
    def _compute_representative_id(self):
        for quality in self:
            quality.representative_id = quality.picking_id.purchase_id.user_id.id
