# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"
    _description = "Sales Analysis Report"

    reseller_id = fields.Many2one('res.partner', 'Reseller', readonly=True)
    commission_percenatge = fields.Float(string="Commission (%)")
    saleable_quantities = fields.Float(string="Qty Saleable")
    reserved_quantities = fields.Float(string="Qty Reserved")

    def _select_sale(self, fields=None):
        return super()._select_sale() + ", s.reseller_id as reseller_id, s.commission_percentage as commission_percenatge, l.saleable_quantities as saleable_quantities, l.reserved_quantities as reserved_quantities "

    def _group_by_sale(self, groupby=''):
        return super(SaleReport, self)._group_by_sale() + ",l.saleable_quantities, l.reserved_quantities "