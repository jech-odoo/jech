# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Purchase Order Email11",

    'summary': """
        This module is to create a purchase order wizard form and add a taxes total in form'.
    """,

    'description': """
        # Task id: 
        This module is to create a purchase order wizard form'.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['base', 'sale', 'purchase','stock'],

    'data': [
        'data/purchase_order_view.xml',
    ],
    
    'installable': True,
}    