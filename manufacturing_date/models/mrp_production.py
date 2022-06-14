# -*- coding: utf-8 -*-
import datetime
import re
from dateutil.relativedelta import relativedelta
from odoo import models,api


class manufacturing_date(models.Model):

    _inherit = 'mrp.production'


    @api.onchange('date_planned_start', 'product_id')
    def _onchange_date_planned_start(self):
        if self.date_planned_start and not self.is_planned:
            self.move_raw_ids = [(1, m.id, {'date': self.date_planned_start}) for m in self.move_raw_ids]
            self.move_finished_ids = [(1, m.id, {'date': self.date_planned_finished}) for m in self.move_finished_ids]
            