{
    # imfromation

    'name': 'Delivery_Date_Shipping ',
    'installable': True,

    # Dependency
    'depends': ['contacts','product', 'sale_management','stock'],
    'data': [
        'views/res_partner_view.xml',
        'views/order_sale.xml',
        'views/stock_picking.xml',
    ],

}
