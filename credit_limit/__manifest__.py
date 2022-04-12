# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'Credit Limit',
   
  
    'description': """
      task id = 2763082
        This module is to create credit_limit and total_receviable amount for customer.
    """,

    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['base','contacts','sale'],
    
     'data': [
        'views/res_partner_view.xml',
    ],

   'installable': True,
}
