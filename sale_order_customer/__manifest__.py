{
    # imfromation

    'name': 'Sale Order customer',
   

    'description': """
     this module are work a customer name with zip code in SO.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['sale_management','contacts'],

    'data': [
        'views/sale_order_view.xml',
    ],

     'installable': True,

}

