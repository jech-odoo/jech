# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons.sale_timesheet.models.project_overview import _to_action_data
from odoo.exceptions import Warning, AccessError


class Project(models.Model):
    _inherit = 'project.project'

    is_customer_material = fields.Boolean("Customer Material")

    def _plan_get_stat_button(self):
        # inherited method to append new stat buttons on project overview form
        stat_buttons = super()._plan_get_stat_button()
        self = self[0]
        product_ids = self.env["product.template"].search(
            [('analytic_id', '=', self.analytic_account_id.id)])
        quotations_ids = self.env["sale.order"].search(
            [('order_line.account_analytic_id', '=', self.analytic_account_id.id)])
        accounts = self.mapped('analytic_account_id.id')

        if self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            sales_stat_button = next(
                (stat_button for stat_button in stat_buttons if stat_button['name'] == _('Sales Orders')), None)
            if sales_stat_button:
                stat_buttons.remove(sales_stat_button)
            # read all the sale orders linked to the projects' tasks
            task_so_ids = self.env['project.task'].search_read([
                ('project_id', 'in', self.ids), ('sale_order_id', '!=', False)
            ], ['sale_order_id'])
            task_so_ids = [o['sale_order_id'][0] for o in task_so_ids]
            sale_orders = self.mapped(
                'sale_line_id.order_id') | self.env['sale.order'].browse(task_so_ids) | quotations_ids
            stat_buttons.extend([{
                'name': _('Sales Orders'),
                'count': len(sale_orders),
                'icon': 'fa fa-dollar',
                'action': _to_action_data(
                    action=self.env.ref('sale.action_orders').sudo(),
                    domain=[('id', 'in', sale_orders.ids)],
                    context={
                        'create': True, 'edit': True, 'delete': False,
                        'default_project_id': self.id,
                        'default_analytic_account_id': self.analytic_account_id.id,
                        'default_visible_project': True
                    }
                )}
            ])
        if self.env.user.has_group('mrp.group_mrp_user'):
            mrp_ids = self.env["mrp.production"].search(
            [('analytic_account_id', '=', self.analytic_account_id.id)])
            stat_buttons.extend([{
                'name': _('Manufacturing') if len(mrp_ids) == 1 else (_('Manufacturings')),
                'count': len(mrp_ids),
                'icon': 'fa fa-wrench',
                'action': _to_action_data(
                    action=self.env.ref('mrp.mrp_production_action').sudo(),
                    domain=[('id', 'in', mrp_ids.ids)],
                    context={'create': True, 'edit': True, 'delete': False, 'default_analytic_id': self.analytic_account_id.id}
                )}
            ])
        stat_buttons.extend([{
            'name': _('Product') if len(product_ids) == 1 else (_('Products')),
            'count': len(product_ids),
            'icon': 'fa fa-th-list',
            'action': _to_action_data(
                action=self.env.ref('stock.product_template_action_product').sudo(),
                domain=[('id', 'in', product_ids.ids)],
                context={'default_analytic_id': self.analytic_account_id.id},
            )},
        ])
        # Checking if PO smart button exists if yes then modifying context to enable Create button
        if self.env.user.has_group('purchase.group_purchase_user'):
            purchase_order_lines = self.env['purchase.order.line'].search(
            [('account_analytic_id', 'in', accounts)])
            purchase_orders = purchase_order_lines.mapped('order_id')
            purchase_stat_button = next(
                (stat_button for stat_button in stat_buttons if stat_button['name'] == _('Purchase Orders')), None)
            if purchase_stat_button:
                purchase_stat_button['action']['data-context'] = {
                    "create": True, "edit": True, "delete": False}

            # If no PO smartbutton found then appending the same
            if not purchase_stat_button:
                stat_buttons.append({
                    'name': _('Purchase Orders'),
                    'count': len(purchase_orders),
                    'icon': 'fa fa-shopping-cart',
                    'action': _to_action_data(
                        action=self.env.ref('purchase.purchase_rfq').sudo(),
                        domain=[('id', 'in', purchase_orders.ids)],
                        context={'create': True, 'edit': True, 'delete': False})
                })
        return stat_buttons

    @api.onchange('name')
    def onchange_product_name(self):
        if self.name and self.search([('name', '=', self.name)]):
            raise Warning(_(
                "This project name is already taken. Please use another name or change the name of the other project(s) first."))

    # def write(self, values):
    #     """
    #         Inheriting the base method so that we can allow the User group to edit only color field.
    #     """
    #     if self.user_has_groups('project.group_project_user') and not self.user_has_groups(
    #             'project.group_project_manager'):
    #         is_color_changed = 'color' in values
    #         if is_color_changed and len(values) == 1:
    #             return super(Project, self.sudo()).write(values)
    #     else:
    #         return super(Project, self).write(values)

