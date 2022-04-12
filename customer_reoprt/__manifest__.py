# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation
    'name': 'Customer Report',
    'installable': True,

    'description': """
        # task id = 2763083
            This module is create a website form to adding a reorder sale order form..

    """,

    # Dependency
    'depends': ['sale','contacts','base'],
    'data': [
        'views/report_view.xml',
        'reports/sale_report_inherit.xml',
        'reports/layout_view.xml',
        # 'reports/footer_layout_view.xml',
       

    ],

}
