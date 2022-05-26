# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = "stock.move"

    # Field declarations
    order_description = fields.Text(
        string="Order Description", compute="_compute_order_description"
    )

    @api.depends("sale_line_id.name", "purchase_line_id.name")
    def _compute_order_description(self):
        """
        Inherited so that we can add value to order description
        """
        for move in self:
            if move.sale_line_id:
                move.order_description = move.sale_line_id.name
            elif move.purchase_line_id:
                move.order_description = move.purchase_line_id.name
            else:
                move.order_description = ""
