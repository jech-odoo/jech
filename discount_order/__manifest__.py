# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'discount_order',
    'installable': True,
  
    'description': """task id = 2763083""",


    # Dependency
    'depends': ['base','sale','account'],
    'data': [
        'views/sale_order_line_view.xml',
        # 'views/account_move_line_view.xml',
        
    ],

}
