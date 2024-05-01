# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

{
    'name':           "Odoo Shipstation Connector",
    'summary':           """
                                    Odoo Shipstation Connector
                                """,
    'description':           """
                                    Odoo Shipstation Connector
                                """,
    'author':           "Webkul Software Pvt. Ltd.",
    'website':           "https://store.webkul.com",
    'category':           'Warehouse',
    'license':           'Other proprietary',
    'version':           '1.0.4',
    'depends':           [
        'odoo_shipping_service_apps',
        'website_sale',
    ],

    'data':           [
        'security/ir.model.access.csv',
        'views/shipstation_config.xml',
        'views/delivery_carrier.xml',
        'views/shipstation_carriers.xml',
        'views/shipstation_stores.xml',
        'views/shipstation_marketplaces.xml',
        'views/shipstation_services.xml',
        'views/shipstation_packages.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/product.xml',
        'views/stock_picking.xml',
        'views/shipstaion_webhooks.xml',
        'views/shipstation_menuitems.xml',
        'data/data.xml',
        'wizards/shipstation_wizard_views.xml',
        'wizards/shipstation_error_info.xml',
    ],
    'images':           ['static/description/Banner.png'],
    'application':           True,
    'installable':           True,
    'price':           99,
    'currency':           'USD',
    'per_init_hook':           'pre_init_check',
}
