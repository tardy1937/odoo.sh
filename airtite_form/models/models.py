# -*- coding: utf-8 -*-

from odoo import models, fields

class AirtiteForm(models.Model):
    _name = 'custom.web.form.airtite_form'
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    date = fields.Date(string='Date')

# from odoo import models, fields, api


# class airtite_form(models.Model):
#     _name = 'airtite_form.airtite_form'
#     _description = 'airtite_form.airtite_form'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

