from odoo import models
from odoo.exceptions import UserError


class StockScrap(models.Model):
    _inherit = 'stock.scrap'


    # create a can_validate variable and get value after method call

    def action_validate(self):
        can_validate = self.env['ir.config_parameter'].sudo().get_param('stock_aacount_validate.ids_scrape')
        print("****************",can_validate)
        if not can_validate:
            raise UserError("Warning")
        return super().action_validate()
     


