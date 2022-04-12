from odoo import models, fields, api
from odoo.osv import expression

class Product(models.Model):
    _inherit = 'product.product'

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     order_id =self._context.get('order_id')
    #     print(":::::::::::::::::::::::", order_id)

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        print("ggggggggggggggggg", self.env.context.get('order_id'))
        order = self.env['sale.order'].browse(self.env.context.get('order_id'))
        if self.env.context.get('order_id'):
            args = args or []
            domain = [('id', 'in', order.order_line.mapped('product_id').ids)]
            return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        return super()._name_search(name=name, args=args, operator=operator, limit=limit, name_get_uid=name_get_uid)


    