# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Stock Rule'",
    'summary': """Add fields and only visible if procure_method = mts_else_mto i stocck rule.""",
    'description': """ 
           In This module create a stock.rule Add a new m2o field (comodel=stock.location) called “Demand Location”
           on stock.rule form view and only visible if procure_method .
    """,
    "author": "Odoo S.A.",
    "website": "http://www.odoo.com/",
    "category": "Customizations",
    "version": "1.0",
    "license": "LGPL-3",
    'depends': ['stock'],
    'data': [
        'views/stock_rule_form_view.xml',
    ],
    
    'demo': [],
    'application': False,
    'installable': True,
    'auto_install': False,
}
