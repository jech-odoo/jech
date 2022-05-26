# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class ProductTemplate(models.TransientModel):
    _name = "product.temp"


    # fields decalration
    product_quantity = fields.Float(string="Quantity", default="1")
    product_uom_id = fields.Many2one("uom.uom", string="Unit of Measure")
    date_planned = fields.Date(string="Scheduled Date", default=fields.Date.today())

    # This method is set a default product uom in another fields.
    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        uom_id = (
            self.env["product.template"].browse(
                self.env.context["active_id"]).uom_id.id
        )
        res["product_uom_id"] = uom_id
        return res

    # method for creating a RFQ
    def create_rfq(self):
        active_model = self.env.context.get('active_model')
        product = self.env[active_model].browse(
            self.env.context["active_id"])
        product_info_id = product.product_variant_id._select_seller(
            quantity=self.product_quantity,
            date=self.date_planned,
            uom_id=self.product_uom_id,
        )
        if product_info_id:
            values = {
                "partner_id": product_info_id.name.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "product_id": product.product_variant_ids.id,
                            "product_qty": self.product_quantity,
                            "name": product.name,
                            "product_uom": self.product_uom_id.id,
                        },
                    )
                ],
            }
            self.env["purchase.order"].create(values)
        else:
            raise UserError(
                (
                    "There is no Vendor define for this Product : "
                    + product.product_variant_ids.name
                    + " Please define Vendor first"
                )
            )

