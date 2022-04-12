{
    # imfromation

    'name': 'Delivery Address 1',
   

    'description': """
        task id = 2763079
        This module is to create a reseller and commision fields to SO form and INV form.
    """,

    # Dependency
    'depends': ['contacts','sale_management','base','account'],

    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
    ],

    'installable': True,

}
