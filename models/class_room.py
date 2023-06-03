from odoo import fields, models


class ClassRoom(models.Model):
    _name = 'class.room'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True)
