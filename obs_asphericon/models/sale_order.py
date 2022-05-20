# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _default_note(self):
        return self.env['ir.config_parameter'].sudo().get_param(
            'account.use_invoice_terms') and self.env.company.invoice_terms or 'Terms and conditions...'

    reseller_id = fields.Many2one("res.partner", string="Reseller")
    shipping_info_id = fields.Many2one("shipping.info", string="Shipping Info")
    number = fields.Integer(related="shipping_info_id.number", string="Number")
    note = fields.Html('Terms and conditions', translate=True, default=_default_note)
    commission_percentage = fields.Float(string="Commission (%)")
    asph_project_ids = fields.Many2many('project.project', string="ASPH Projects", compute="_compute_asph_project_ids")


    @api.depends('order_line.account_analytic_id')
    def _compute_asph_project_ids(self):
        for order in self:
            projects = self.env['project.project'].search(
                [('analytic_account_id', 'in', order.order_line.mapped('account_analytic_id').ids)])
            order.asph_project_ids = [(4, project.id) for project in projects] or []

    @api.onchange('partner_id')
    def _onchange_partner_id_incoterms(self):
        self.incoterm = self.partner_id.sales_incoterm_id.id or False

    def action_open_create_project(self):
        return {
            'name': 'Create a Project',
            'type': 'ir.actions.act_window',
            'res_model': 'project.template.wizard',
            'target': 'new',
            'views': [[False, "form"]],
        }

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'reseller_id': self.reseller_id.id,
            'commission_percentage': self.commission_percentage,
        })
        return res

    def update_prices(self):
        self.ensure_one()
        lines_to_update = []
        for line in self.order_line.filtered(
                lambda line: not line.display_type and not line.product_id.ignore_sales_price):
            product = line.product_id.with_context(
                partner=self.partner_id,
                quantity=line.product_uom_qty,
                date=self.date_order,
                pricelist=self.pricelist_id.id,
                uom=line.product_uom.id
            )
            price_unit = self.env['account.tax']._fix_tax_included_price_company(
                line._get_display_price(product), line.product_id.taxes_id, line.tax_id, line.company_id)
            if self.pricelist_id.discount_policy == 'without_discount' and price_unit:
                price_discount_unrounded = self.pricelist_id.get_product_price(product, line.product_uom_qty,
                                                                               self.partner_id, self.date_order,
                                                                               line.product_uom.id)
                discount = max(0, (price_unit - price_discount_unrounded) * 100 / price_unit)
            else:
                discount = 0
            lines_to_update.append((1, line.id, {'price_unit': price_unit, 'discount': discount}))
        if lines_to_update:
            self.update({'order_line': lines_to_update})
            self.show_update_pricelist = False
            self.message_post(body=_("Product prices have been recomputed according to pricelist <b>%s<b> ",
                                     self.pricelist_id.display_name))

    def action_view_project_ids(self):
        res = super(SaleOrder, self).action_view_project_ids()
        res['domain'] = ['|', ('id', 'in', self.project_ids.ids), ('id', 'in', self.asph_project_ids.ids)]
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    saleable_quantities = fields.Float(
        string="Saleable", compute="_compute_saleable_quantities", store=True)
    reserved_quantities = fields.Float(string="Reserved", compute="_compute_reserved_quantities", store=True)
    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account', store=True,
                                          compute='_compute_account_analytic_id', readonly=False)
    shipping_info_id = fields.Many2one("shipping.info", string="Shipping Info")

    @api.depends('product_id', 'scheduled_date')
    def _compute_account_analytic_id(self):
        for rec in self:
            if not rec.account_analytic_id:
                default_analytic_account = rec.env['account.analytic.default'].sudo().account_get(
                    product_id=rec.product_id.id,
                    partner_id=rec.order_id.partner_id.id,
                    user_id=rec.env.uid,
                    date=rec.scheduled_date,
                    company_id=rec.company_id.id,
                )
                rec.account_analytic_id = default_analytic_account.analytic_id

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        if not self.product_uom or not self.product_id:
            self.price_unit = 0.0
            return
        if self.order_id.pricelist_id and self.order_id.partner_id and not self.product_id.ignore_sales_price:
            product = self.product_id.with_context(
                lang=self.order_id.partner_id.lang,
                partner=self.order_id.partner_id,
                quantity=self.product_uom_qty,
                date=self.order_id.date_order,
                pricelist=self.order_id.pricelist_id.id,
                uom=self.product_uom.id,
                fiscal_position=self.env.context.get('fiscal_position')
            )
            self.price_unit = self.env['account.tax']._fix_tax_included_price_company(self._get_display_price(product),
                                                                                      product.taxes_id, self.tax_id,
                                                                                      self.company_id)

    @api.depends('order_id.picking_ids', 'saleable_quantities')
    def _compute_reserved_quantities(self):
        for line in self:
            line.reserved_quantities = 0.0
            for picking in line.order_id.picking_ids:
                if picking.state not in ['done', 'cancel']:
                    for move_line_id in picking.move_line_ids_without_package:
                        if move_line_id.product_id == line.product_id:
                            line.reserved_quantities = move_line_id.product_uom_qty

    @api.depends('qty_delivered')
    def _compute_saleable_quantities(self):
        for line in self:
            line.saleable_quantities = 0.0
            location_ids = self.env['stock.location'].search([('is_saleable_quantities', '=', True), ('company_id', '=', line.order_id.company_id.id)])
            quants = location_ids.quant_ids
            for quant in quants:
                if quant.product_id == line.product_id:
                    line.saleable_quantities += quant.available_quantity

    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        if self.product_id.ignore_sales_price:
            return
        return super()._onchange_discount()

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res['analytic_account_id'] = self.account_analytic_id.id
        return res

