{
    # imfromation

    'name': 'product_purches ',
    'installable': True,

    # Dependency
    'depends': ['contacts', 'sale_management','delivery_barcode','base','sale'],
    'data': [
        'views/partner_order.xml',
        'security/ir.model.access.csv',
    ],

}
