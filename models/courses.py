from odoo import fields, models, _


class Courses(models.Model):
    _name = 'logic.courses'
    _rec_name = 'name'
    _inherit = 'mail.thread'

    name = fields.Char(string='Course name')
    type = fields.Selection([
        ('indian', 'Indian'),
        ('international', 'International'),
    ], string='Type')
    board_registration = fields.Boolean(string='Board registration')
