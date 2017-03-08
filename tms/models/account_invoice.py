# -*- coding: utf-8 -*-
# Copyright 2012, Israel Cruz Argil, Argil Consulting
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    waybill_ids = fields.One2many(
        'tms.waybill', 'invoice_id', string="Waybills", readonly=True)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.payment_method_id = self.partner_id.payment_method_id
