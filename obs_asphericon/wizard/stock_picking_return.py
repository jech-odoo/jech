# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ReturnPickingLine(models.TransientModel):
    _inherit = "stock.return.picking.line"

    # Field Declarations
    order_description = fields.Text(string='Order Description', compute='_compute_order_description')

    # Compute methods
    @api.depends('move_id.sale_line_id.name', 'move_id.purchase_line_id.name')
    def _compute_order_description(self):
        """
        Inherited so that we can add value to order description from sale line
        or purchase line linked to the selected stock move.
        """
        for line in self:
            if line.move_id.sale_line_id:
                line.order_description = line.move_id.sale_line_id.name
            elif line.move_id.purchase_line_id:
                line.order_description = line.move_id.purchase_line_id.name
            else:
                line.order_description = ''
