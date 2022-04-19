{
    # imfromation

    'name': 'website payslip',
   

    'description': """
       this module create a new payslip and view website page login a portal user.. 
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['website','base','hr_payroll','hr'],

    'data': [
        'views/portal_website_view.xml',
        # 'report/payslip_report.xml',
        # 'views/template.xml',
        
    ],

     'installable': True,
     'license': 'LGPL-3',

}

