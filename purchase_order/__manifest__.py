# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'Purchase Order',
    'installable': True,
  
    'description': """this module is create a purchase order form and add a m2o fields to create a receipt to user.""",


    # Dependency
    'depends': ['base','purchase_stock','stock','purchase'],
    'data': [
        'views/stock_picking_view.xml',
    ],

}
