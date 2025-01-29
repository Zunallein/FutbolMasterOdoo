# -*- coding: utf-8 -*-
{
    'name': "futbol_master",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/entrenador.xml',
        'views/equipo.xml',
        'views/jugador.xml',
        'views/club.xml',
        'views/estadio.xml',    
        'views/partido.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'futbol_master/css/style.css',
    ]},
}
