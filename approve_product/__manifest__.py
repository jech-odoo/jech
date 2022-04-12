{
    # imfromation

    'name': 'Approve Product ',
   

    'description': """
         Task id:  2763079
           This module is to create a approve_product to  approve a product user and administrator.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['contacts', 'sale_management', 'delivery_barcode', 'stock','base'],

    'data': [
        'views/sale_order.xml',
    ],

     'installable': True,

}

