# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmClaims(models.Model):
    _inherit = 'crm.claim'


    is_expense = fields.Boolean(default=False, string='Is Expense')
    parent_id = fields.Many2one('hr.department', 'Deparment')
    cost_without_vat = fields.Float(string="Cost Without Vat", digits=(6, 2))
    invoice_ids = fields.Many2many('account.invoice', string='Invoices')


class CrmClaimsSequence(models.Model):
    _inherit = 'crm.claim'


    name = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
            'crm.claim') or 'New'
            result = super(CrmClaimsSequence, self).create(vals)
            return result
