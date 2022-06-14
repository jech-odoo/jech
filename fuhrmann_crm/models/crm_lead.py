# -*- coding: utf-8 -*-

from bs4 import Declaration
from odoo import models, fields,api
from odoo.addons.crm.models import crm_stage


class CRMLead(models.Model):
    _inherit = "crm.lead"

    priority = fields.Selection(
        crm_stage.AVAILABLE_PRIORITIES, string='Priority', index=True,
        default=crm_stage.AVAILABLE_PRIORITIES[0][0], tracking=True)
    probability = fields.Float(
        'Probability', group_operator="avg", copy=False,
        compute='_compute_probabilities', readonly=False, store=True, tracking=True)

    # fields Declaration
    recurring_revenue_yearly = fields.Monetary('Expected YRR', store=True,
                                              compute="_compute_recurring_revenue_yearly", currency_field='company_currency')

    recurring_revenue_annual_prorated = fields.Monetary(
        'Expected ARR', store=True,compute="_compute_recurring_revenue_annual_prorated", currency_field='company_currency')

    
    @api.depends('recurring_revenue', 'recurring_plan.number_of_months')
    def _compute_recurring_revenue_yearly(self):
        for lead in self:
            lead.recurring_revenue_yearly = ((lead.recurring_revenue or 0.0) / (lead.recurring_plan.number_of_months or 1)) * 12
         
    @api.depends('recurring_revenue_monthly', 'probability')
    def _compute_recurring_revenue_annual_prorated(self):
        for lead in self:
            lead.recurring_revenue_annual_prorated = (lead.recurring_revenue_yearly or 0.0) * (lead.probability or 0) / 100.0
