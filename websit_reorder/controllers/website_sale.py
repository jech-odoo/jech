# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http


class PortalReorder(http.Controller):

    @http.route('/reorder_website', type='http', auth="user", website=True)
    def reorder(self, **kwargs):
        old_order = http.request.env['sale.order'].browse(int(kwargs.get('order_id')))
        new_order = http.request.website.sale_get_order(force_create=True)
        new_order.order_line.unlink()

        for line in old_order.order_line:
            new_order._cart_update(product_id=line.product_id.id, add_qty=line.product_uom_qty)
    
        # [new_order._cart_update(product_id=line.product_id.id, add_qty=line.product_uom_qty)for line in old_order.order_line]    
        return http.request.redirect('/shop/cart')
 





  