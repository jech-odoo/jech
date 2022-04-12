{
    # imfromation

    'name': 'Sale Order Product Line',
   

    'description': """
       this module are worked a particular customer,order,product view in product line.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['sale_management','contacts','stock'],

    'data': [
        'views/sale_order_view.xml',
    ],

     'installable': True,

}

