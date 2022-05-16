# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation
    'name': 'Quality Check',
    'installable': True,

    'description': """This module is create a Quality Check, that is linked to a picking, is moved to the state “Passed”, automatically process the linked picking.""",

    # Dependency
    'depends': ['quality_control','sale_management','stock'],
    'data': [
    ],

}
