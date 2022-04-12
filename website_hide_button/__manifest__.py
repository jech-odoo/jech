{
    # imfromation

    'name': 'website Button',
   

    'description': """
        this module is manage a print button hide in website sale order form.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['website','base','sale','account'],

    'data': [
        'views/sale_website_view.xml',
    ],

     'installable': True,
     'license': 'LGPL-3',

}

