from odoo import fields,models


class LogicBranches(models.Model):
    _name = 'logic.branches'
    _inherit = 'mail.thread'
    _rec_name = 'branch_name'

    branch_name = fields.Char('Branch name')
