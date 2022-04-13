# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    # imfromation

    'name': 'Manufacturing',
   

    'description': """
       this module to create a start,end and done in action menu. 
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
     'depends': ['base','mrp'],

    'data': [
         'views/mrp_workorder_view.xml',
        
    ],

     'installable': True,
     

}


