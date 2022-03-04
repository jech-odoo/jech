# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'Delivery_Date_Shipping ',
    'installable': True,
    'description': """task id = 2763078""",

    # Dependency
    'depends': ['contacts','product', 'sale_management','stock'],
    'data': [
        'views/res_partner_view.xml',
        'views/order_sale.xml',
        'views/stock_picking.xml',
    ],

}
