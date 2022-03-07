# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'Product Purchase ',
    'installable': True,
  
    'description': """task id = 2763080""",


    # Dependency
    'depends': ['contacts','base','sale','product'],
    'data': [
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',
    ],

}
