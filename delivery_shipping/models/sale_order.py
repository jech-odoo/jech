# -*- coding: utf-8 -*-

from odoo import models,fields,api
import datetime

class SaleOrder(models.Model):

  
    _inherit ='sale.order'


    #------------------------
    #  fields Declaration
    #------------------------

    requested_date = fields.Datetime(string='Appointment Date')
   

    #------------------------------------------------------------------
    # compute fields //write comput attribut(compute='_delivery_date',)
    #------------------------------------------------------------------

    commitment_date = fields.Datetime('Delivery Date', copy=False,
                                      states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
                                      help="This is the delivery date promised to the customer. "
                                           "If set, the delivery order will be scheduled based on "
                                           "this date rather than product lead times.", readonly=False,compute='_delivery_date')

    #-----------------------
    # method declaration
    #----------------------
    
    @api.depends('requested_date')
    def _delivery_date(self):
        for record in self:
            if record.requested_date and record.partner_id.day_to_delivrer > 0:
                record.commitment_date = record.requested_date - datetime.timedelta(days=record.partner_id.day_to_delivrer)


   
    def action_confirm(self):
        print("confiem method")
        record = super(SaleOrder , self).action_confirm()
        for data in self.picking_ids:
            data.requested_date = self.requested_date
        return record
