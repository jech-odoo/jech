# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models
from odoo.tests import Form


class QualityCheck(models.Model):

    _inherit = 'quality.check'

    def do_pass(self):
        res = super().do_pass()
        if self.picking_id.move_ids_without_package:
            for move in self.picking_id.move_ids_without_package.filtered(lambda x: x.product_id == self.product_id):
                    move.quantity_done = move.forecast_availability
                    picking = self.picking_id.with_context(skip_backorder=False)
                    action_data = picking.button_validate()
                    if move.product_uom_qty != move.quantity_done:
                        backorder_wizard = Form(self.env['stock.backorder.confirmation'].with_context(action_data['context'])).save()
                        backorder_wizard.process()
        return res
