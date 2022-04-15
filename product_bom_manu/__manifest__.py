{
    # imfromation

    'name': 'Product Manufacturing',
    'installable': True,

    'description': """ this module is create a add a new relational fields and view selected customer name.""",

    'author': 'Odoo Ps',
    'version': '15.0',
    # Dependency
    'depends': ['mrp','stock'],

    'data': [
        'views/product_template_view.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',

}
