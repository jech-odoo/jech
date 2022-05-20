# -*- coding: utf-8 -*-

from odoo import models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('partner_id')
    def _onchange_partner_id_incoterms(self):
        self.incoterm_id = self.partner_id.purchase_incoterm_id.id or False

    def _prepare_picking(self):
        res = super()._prepare_picking()
        if self.partner_ref:
            origin = '{} ({})'.format(res['origin'], self.partner_ref)
            res['origin'] = origin
        return res

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


    def write(self, values):
        if 'date_planned' in values:
            for line in self:
                if line.order_id.state == 'purchase':
                    line.order_id.message_post_with_view('obs_asphericon.track_po_line_delivery_date',
                                values={'line': line, 'date_planned': values.get('date_planned')},
                                subtype_id=self.env.ref('mail.mt_note').id)
        return super().write(values)

    @api.onchange('product_qty', 'product_uom')
    def _onchange_quantity(self):
        price_unit_ignored = self.price_unit
        name_ignored = self.name
        res = super()._onchange_quantity()
        if not self.product_id:
            return
        params = {'order_id': self.order_id}
        seller = self.product_id._select_seller(
            partner_id=self.partner_id,
            quantity=self.product_qty,
            date=self.order_id.date_order and self.order_id.date_order.date(),
            uom_id=self.product_uom,
            params=params)
        if self.product_id.ignore_vendor_pricelists:
            if price_unit_ignored != 0:
                self.price_unit = price_unit_ignored
                self.name = name_ignored
            else:
                self.price_unit = seller.price
            return
        return res

    @api.onchange('product_qty', 'product_uom')
    def _onchange_qty_set_discount(self):
        if not self.product_id:
            return
        params = {'order_id': self.order_id}
        seller = self.product_id._select_seller(
            partner_id=self.partner_id,
            quantity=self.product_qty,
            date=self.order_id.date_order and self.order_id.date_order.date(),
            uom_id=self.product_uom,
            params=params)
        discount_ignored = self.discount
        if seller and not self.product_id.ignore_vendor_pricelists:
            self.discount = seller.discount
            return
        if seller and self.product_id.ignore_vendor_pricelists and not self.discount != 0:
            self.discount = discount_ignored or seller.discount
