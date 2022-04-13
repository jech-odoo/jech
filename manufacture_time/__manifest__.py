# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation
    'name': 'Manufacturing',
    'installable': True,

    # 'description': """task id = 2763083""",

    # Dependency
    'depends': ['base','mrp'],
    'data': [
        'views/mrp_workorder_view.xml',
    ],

}
