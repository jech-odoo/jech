# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api
import datetime


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # -------------------------
    #  fields Declaration
    # --------------------------

    requested_date = fields.Datetime(string="Appointment Date")

    # ------------------------
    # method declaration
    # -------------------------

    @api.onchange('requested_date')
    def _onchange_date(self):
        for record in self:
            if record.requested_date and record.partner_id.day_to_delivrer > 0:
                record.scheduled_date = record.requested_date - datetime.timedelta(
                    days=record.partner_id.day_to_delivrer)
