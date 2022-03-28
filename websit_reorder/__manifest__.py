# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation
    'name': 'Website Reorder',
    'installable': True,

    'description': """
         task id = 2763083
            This module is create a website form to adding a reorder sale order form..

    """,

    # Dependency
    'depends': ['base','website','sale','website_sale'],
    'data': [
        'views/sale_website_view.xml',
      
    ],

}