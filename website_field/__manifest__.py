{
    # imfromation

    'name': 'Website',
   

    'description': """
      this module create char field and view field in website.
    """,
    'author': 'Odoo Ps',
    'version': '15.0',

    # Dependency
    'depends': ['website','crm'],

    'data': [
        'data/website_contact.xml',
    ],

     'installable': True,

}

