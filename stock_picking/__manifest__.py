# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation
    'name': 'Stock Picking',
    'installable': True,

    # 'description': """task id = 2763083""",

    # Dependency
    'depends': ['base', 'sale', 'purchase','stock'],
    'data': [
        'views/stock_picking_view.xml',
    ],

}
