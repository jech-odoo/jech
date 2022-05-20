# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    analytic_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account',
        inverse='_inverse_analytic_id', compute="_compute_analytic_id", readonly=False, search="_search_analytic_id")

    project_count = fields.Integer(compute="_compute_project_count")
    tag_ids = fields.Many2many("product.tags", string="Tags")
    is_asph_service_product = fields.Boolean(string="ASPH Service")
    ignore_sales_price = fields.Boolean(string="Ignore Sales Prices", related="categ_id.ignore_sales_price")
    ignore_vendor_pricelists = fields.Boolean(string="Ignore Vendor Pricelists", related="categ_id.ignore_vendor_pricelists")

    @api.onchange('categ_id')
    def onchange_categ_id(self):
        if self.categ_id and self.type != 'consu':
            self.is_asph_service_product = False

    @api.depends_context('company')
    def _compute_analytic_id(self):
        company = self.env.company.id
        res = self.env['account.analytic.account']._get_analytic_account(self.ids, company_id=company)
        for p in self:
            p.analytic_id = res[0].get(p.id) or False

    def _inverse_analytic_id(self):
        for product in self:
            self.env['ir.property']._set_multi('analytic_id', product._name, {product.id: product.analytic_id})

    def _search_analytic_id(self, operator, value):
        analytic_id = self.search([]).filtered(lambda x : x.analytic_id.id == value )
        return [('id', 'in', [x.id for x in analytic_id] if analytic_id else False )]

    @api.depends('analytic_id')
    def _compute_project_count(self):
        Project = self.env["project.project"]
        for product in self:
            product.project_count = Project.search_count(
                [('analytic_account_id', '=', product.analytic_id.id)])

    def action_open_projects(self):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'sale_timesheet.project_timesheet_action_client_timesheet_plan')
        action['domain'] = [('analytic_account_id', '=', self.analytic_id.id)]
        action['context'] = {'create': False}
        return action

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.product_variant_id.id:
            if "analytic_id" in vals and not vals['analytic_id'] is False:
                self.env["account.analytic.default"].create({
                    "product_id": res.product_variant_id.id,
                    "analytic_id": vals.get('analytic_id'),
                    "is_from_product": True
                })
        return res

    def write(self, vals):
        if 'analytic_id' in vals:
            AnalyticDefault = self.env["account.analytic.default"]
            for product in self:
                AnalyticDefault.search([('analytic_id', '=', product.product_variant_id.analytic_id.id), (
                    'product_id', '=', product.product_variant_id.id), ('is_from_product', '=', True)], limit=1).unlink()
        if vals.get('analytic_id') and vals.get('analytic_id') != False:
            AnalyticDefault.create({
                "product_id": self.product_variant_id.id,
                "analytic_id": vals.get('analytic_id'),
                "is_from_product": True
            })
        return super().write(vals)


class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.id:
            if "analytic_id" in vals and not vals['analytic_id'] is False:
                self.env["account.analytic.default"].create({
                    "product_id": res.id,
                    "analytic_id": vals.get('analytic_id'),
                    "is_from_product": True
                })
        return res

    def write(self, vals):
        if 'analytic_id' in vals:
            AnalyticDefault = self.env["account.analytic.default"]
            for product in self:
                AnalyticDefault.search([('analytic_id', '=', product.analytic_id.id), (
                    'product_id', '=', product.product_variant_id.id), ('is_from_product', '=', True)], limit=1).unlink()
        if vals.get('analytic_id') and vals.get('analytic_id') != False:
            AnalyticDefault.create({
                "product_id": self.id,
                "analytic_id": vals.get('analytic_id'),
                "is_from_product": True
            })
        return super().write(vals)

    def action_open_projects(self):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'sale_timesheet.project_timesheet_action_client_timesheet_plan')
        action['domain'] = [('analytic_account_id', '=', self.analytic_id.id)]
        action['context'] = {'create': False}
        return action

    @api.onchange('categ_id')
    def onchange_categ_id(self):
        if self.categ_id and self.categ_id.product_type != 'consu':
            self.is_asph_service_product = False