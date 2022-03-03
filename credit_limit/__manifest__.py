# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'credit_limit',
    'installable': True,
  
    'description': """task id = 2763082""",


    # Dependency
    'depends': ['base','contacts','sale'],
     'data': [
        'views/res_partner_view.xml',
    ],
}
