{
    # imfromation

    'name': 'product_purches ',
    'installable': True,
  
    'description': """task id = 2763080""",


    # Dependency
    'depends': ['contacts','sale_management','delivery_barcode','base','sale'],
    'data': [
        'views/partner_order.xml',
        'security/ir.model.access.csv',
    ],

}
