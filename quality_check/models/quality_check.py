# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _, api


class QualityCheck(models.Model):

    _inherit = 'quality.check'

    def do_pass(self):
        res = super().do_pass()
        if self.picking_id.move_ids_without_package:
            for move in self.picking_id.move_ids_without_package:
                if move.product_id==self.product_id:
                    move.quantity_done = move.forecast_availability
                    picking = self.picking_id.with_context(skip_backorder=False)
                    picking.button_validate()
        return res




