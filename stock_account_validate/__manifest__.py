{
    # imfromation

    'name': 'Stock Account Validate',
   

    'description': """
        this module create boolean field and fields are false than validate button are throw user error.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['stock'],

    'data': [
        'views/res_config_settings_view.xml',
    ],

     'installable': True,

}

