# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.s
from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    secound_discount = fields.Float(string="2nd disc%")

    def _get_price_total_and_subtotal(self, price_unit=None, quantity=None, discount=None, currency=None, product=None,
                                      partner=None, taxes=None, move_type=None):
        # self.ensure_one()
        res = super()._get_price_total_and_subtotal(price_unit=price_unit, quantity=quantity, discount=discount,
                                                    currency=currency, product=product, partner=partner, taxes=taxes,
                                                    move_type=move_type)
        print("res  : ", res.get('price_subtotal'))
        print("2nd disc,", self.secound_discount)
        price_subtotal = res.get('price_subtotal') - ((res.get('price_subtotal') * self.secound_discount) / 100)
        res['price_subtotal'] = price_subtotal
        print("**res**", res)
        return res
