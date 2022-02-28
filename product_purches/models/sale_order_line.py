############## sales order ###################
from odoo import fields,models,api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        for line in self:
            if line.order_id.partner_id:
                if line.order_id.partner_id.product_uom_detail_ids:
                    uom_details_ids = line.order_id.partner_id.product_uom_detail_ids
                    for record in uom_details_ids:
                        if line.product_id == record.product_id:
                            line.product_uom = record.uom_id
        return res