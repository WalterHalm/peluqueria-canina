# -*- coding: utf-8 -*-
{
    'name': "sale_order_payment",

    'summary': "Permite registrar pagos parciales en pedidos de venta antes de facturar.",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_payment_views.xml',
        'views/sale_order_views.xml',        
        'views/menu_items.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}

