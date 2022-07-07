# -*- coding: utf-8 -*-
# Copyright 2017 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, _


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    def dhl_rate_shipment(self, orders):
        return {'success': True,
                'price': 0,
                'error_message': False,
                'warning_message': False}

    delivery_type = fields.Selection(selection_add=[('dhl', "DHL")], ondelete={'dhl': lambda recs: recs.write({'delivery_type': 'fixed', 'fixed_price': 0})})

    dhl_user_id = fields.Char(string="DHL User ID")
    dhl_password = fields.Char(string="DHL Password")
    dhl_shipment_option = fields.Selection([('DOOR','Door')], default="DOOR", string="DHL Shipment Option")
    dhl_parcel_type = fields.Selection([('SMALL','Small'),('MEDIUM','Medium'),('LARGE','Large'),('PALLET','Pallet')], default="SMALL", string="DHL Parcel Type")
    dhl_account_id = fields.Char(string="DHL Account ID")
