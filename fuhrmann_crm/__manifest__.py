# -*- coding: utf-8 -*-
{
    'name': 'Fuhrmann CRM',
    'summary': 'Customization CRM Lead form.',
    "license": "LGPL-3",
    'website': 'https://www.odoo.com',
    'version': '1.0',
    'author': 'Odoo SA',
    'description': """
        This module allows only the admin should add new records 
        on the 'Tags' field in the CRM form view.
        In this module 'Priority' and 'Probability' are tracking fields.
    """,
    'category': 'CRM',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
