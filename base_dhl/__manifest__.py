# -*- coding: utf-8 -*-
# Copyright 2017 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "DHL Shipping",
    'description': "DHL Shipping",
    'author': 'Onestein',
    'website': 'http://www.onestein.eu',
    'category': 'Warehouse',
    'version': '15.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'delivery',
    ],
    'data': [
        'data/stock_package_type.xml',
        'views/delivery_carrier_view.xml',
    ],
}
