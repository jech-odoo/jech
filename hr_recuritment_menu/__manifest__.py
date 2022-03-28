# -*- coding: utf-8 -*-
{
    'name':"Hr Recuritment Menu",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

   
  
    # any module necessary for this one to work correctly
    'depends': ['hr_recruitment','contacts'],

    # always loaded
    'data': [
        'views/hr_job_menu_view.xml',
    ],
    # only loaded in demonstration mode
   
    ],
}
