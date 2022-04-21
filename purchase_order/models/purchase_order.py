# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, api


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    def _prepare_picking(self):
        res = super()._prepare_picking()
        res.update({'stock_user_id': self.user_id.id})
        return res
