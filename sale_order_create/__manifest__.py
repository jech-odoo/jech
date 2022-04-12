{
    # imfromation

    'name': 'Sale Order Create',
   

    'description': """
    this module is manage a field in sale order form.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['sale_management'],

    'data': [
        'views/sale_order_view.xml',
    ],

     'installable': True,

}

