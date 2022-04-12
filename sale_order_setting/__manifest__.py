{
    # imfromation

    'name': 'Sale Order Field',
   

    'description': """
        this module creates a relational field in res_config_setting. 
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['sale_management'],

    'data': [
        'views/res_config_settings_view.xml',
    ],

     'installable': True,

}

