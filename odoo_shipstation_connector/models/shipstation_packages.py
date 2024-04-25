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

from odoo import fields, models, api


class ShipstationPackages(models.Model):
    _name = 'shipstation.packages'
    _description = 'ShipStation Packages'

    name = fields.Char(string='Package Name')
    carrier_code = fields.Many2one('shipstation.carriers', string='Carrier Code')
    package_code = fields.Char(string='Package Code')
    is_domestic = fields.Boolean(string='Is Domestic')
    is_international = fields.Boolean(string='Is International')
    shipstation_user_id = fields.Many2one('shipstation.configuration', string="Shipstation User")
