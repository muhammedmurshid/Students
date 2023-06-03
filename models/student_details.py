from odoo import fields, models


class StudentsDetails(models.Model):
    _name = 'student.details'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', copy=False)
    email = fields.Char(string='Email address')
    phone_number = fields.Char(string='Mobile number')
