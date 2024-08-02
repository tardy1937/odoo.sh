# -*- coding: utf-8 -*-
{
    'name': "airtite_form",

    'summary': "Custom Airtite Form.",

    # 'description': """
    # """,

    'author': "Dome Software",
    'website': "https://dome.software",

    'category': 'Website',
    'version': '0.1.1',

    'depends': ['base', 'website'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}

