{
    # imfromation

    'name': 'POS Zip',
   

    'description': """
       this module is create a manage a customer postcode are not selected than show popup and enter postcode in pos.
       
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['point_of_sale','base'],

    'data': [
        'views/pos_view.xml',
    ],

    'assets': {
        'point_of_sale.assets': [
            'pos_zip/static/src/js/ProductScreen.js',
        ],
        'web.assets_qweb': [
            'pos_zip/static/src/xml/**/*',
        ],
    },

     'installable': True,
     'license': 'LGPL-3',

}

