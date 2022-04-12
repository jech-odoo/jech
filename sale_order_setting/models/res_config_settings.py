# -*- coding: utf-8 -*-

from unicodedata import name
from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    customer_id = fields.Many2one('res.partner',config_parameter='sale_order_setting.default_customer_id')

    
