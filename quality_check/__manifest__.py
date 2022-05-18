# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Quality Check",
    'summary': """Manage quantity of 'down payment' product in regular invoice""",
    'description': """ 
           In This module create a Quality Check, that is linked to a picking, 
           is moved to the state 'Passed', automatically process the linked picking.
    """,
    "author": "Odoo S.A.",
    "website": "http://www.odoo.com/",
    "category": "Customizations",
    "version": "1.0",
    "license": "LGPL-3",
    'depends': ['quality_control','sale_management'],
    

    'demo': [],
    'application': False,
    'installable': True,
    'auto_install': False,
}
