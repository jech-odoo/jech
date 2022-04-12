# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ids_scrape = fields.Boolean('Scrape',config_parameter='stock_account_validate.ids_scrape')

    #  set and get vaules and fields data are saved..

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'stock_aacount_validate.ids_scrape', self.ids_scrape)

        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            ids_scrape=ICPSudo.get_param('stock_aacount_validate.ids_scrape'),
        )
        return res


                


            

