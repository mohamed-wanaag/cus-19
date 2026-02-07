# -*- coding: utf-8 -*-
# Powered by Wanaag Solutions
# © 2025 Wanaag Solutions (https://wanaag.odoo.com)
# All Rights Reserved.

{
    'name': 'Remove Powered by Odoo from Website & Add Custom Text',
    'version': '19.0.1.0.0',
    'summary': 'Hide or replace the "Powered by Odoo" footer message with your own custom HTML content.',
    'description': """
This free module lets you fully customize or hide the default "Powered by Odoo" footer message.
Easily configure your own footer text or HTML through the Settings menu.

✨ Features:
• Toggle the visibility of "Powered by Odoo"
• Add rich HTML content (links, colors, alignment)
• Real-time updates, no page refresh needed
• Responsive and white-label friendly
    """,
    'author': 'Wanaag Solutions',
    'website': 'https://wanaag.odoo.com/',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/res_config_settings_view.xml',
        'views/brand_promotion_override.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
