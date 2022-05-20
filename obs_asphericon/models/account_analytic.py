# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    def _get_analytic_account(self, product_ids, company_id=None):
        result = []
        company_id = company_id or self.env.company.id
        Property = self.env['ir.property'].with_company(company_id)
        analytic_id = Property._get_multi('analytic_id', 'product.template', product_ids)
        result.append(analytic_id)
        return result