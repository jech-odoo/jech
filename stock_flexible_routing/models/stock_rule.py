# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockRule(models.Model):

    _inherit = 'stock.rule'

    # -------------------------
    #  fields Declaration
    # --------------------------
    demand_location_id = fields.Many2one('stock.location', string='Demand Location')

    # --------------------------------
    #  method for change value in fields
    # --------------------------------
    @api.onchange('procure_method')
    def _onchange_procure_method(self):
        if self.procure_method != 'mts_else_mto':
            self.demand_location_id = False

    # --------------------------------
    #  method for change the text message”
    # -------------------------------
    def _get_message_dict(self):
        res = super()._get_message_dict()
        source = self.location_src_id and self.location_src_id.display_name or _('Source Location')
        destination = self.location_id and self.location_id.display_name or _('Destination Location')
        operation = self.picking_type_id and self.picking_type_id.name or _('Operation Type')
        new = self.demand_location_id and self.demand_location_id.display_name or ('Demand Location')
        if self.procure_method == 'mts_else_mto' and self.demand_location_id:
            suffix = _(
                "<br>If the products are not available in <b>%s</b>, a rule will be triggered to bring products in <b>%s</b>.", source, new)
            res.update({'pull': _('When products are needed in <b>%s</b>, <br/> <b>%s</b> are created from <b>%s</b> to fulfill the need.', destination, operation, source) + suffix,
                       'push': _('When products arrive in <b>%s</b>, <br/> <b>%s</b> are created to send them in <b>%s</b>.', source, operation, destination)})
        return res

    # ------------------------------------------------
    #  method for change destination location of stock”
    # ------------------------------------------------
    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        res=super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        if self.demand_location_id:
            res.update({
                'location_dest_id': self.demand_location_id.id,
            })
        return res
