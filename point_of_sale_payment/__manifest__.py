{
    # imfromation

    'name': 'Point Of Sale Payment',
   

    'description': """
       this module is manage a customer are not selected than view popup.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['point_of_sale','base'],

    'data': [
       
    ],

    'assets': {
        'point_of_sale.assets': [
            'point_of_sale_payment/static/src/js/ProductScreen.js',
        ],
        'web.assets_qweb': [
            # 'point_of_sale_payment/static/src/xml/**/*',
        ],
    },

     'installable': True,
     'license': 'LGPL-3',

}

