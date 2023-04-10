# -*- coding: utf-8 -*-
{
    'name': 'Odoo Hide Menu User',
    'version': '16.0.1.0.0',
    'summary': 'Odoo Hide Menu User',
    'description': 'Odoo Hide Menu User',
    'category': 'Extra Tools',
    'author': 'Wahyu',
    'company': '-',
    'maintainer': '-',
    'website': "",
    'depends': ['base'],
    'data': [
        'views/res_users.xml',
        'security/security.xml'
    ],
    'license': 'LGPL-3',
    'images': [
        'static/description/icon.png',
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
