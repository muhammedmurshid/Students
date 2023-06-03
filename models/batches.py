from odoo import fields, models


class LogicBatches(models.Model):
    _name = 'logic.batches'
    _rec_name = 'batch_name'
    _inherit = 'mail.thread'

    batch_name = fields.Char(string='Batch name', required=True)
    status = fields.Selection([('draft', 'Draft'), ('approve', 'Approved'), ('reject', 'Rejected')], string='Status',
                              default='draft')
    branch_name = fields.Many2one('logic.branches', string='Branch')
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    class_type = fields.Selection([('online', 'Online'), ('offline', 'Offline')], string='Class type')
    created_by = fields.Char(string='Created by', default=lambda self: self.env.user.name, readonly=True)
    no_of_students = fields.Integer(string='No.of students')
    handled_by = fields.Many2one('hr.employee', string='Handled by')
    admission_status = fields.Selection([('open', 'Admission Open'), ('closed', 'Admission Closed')],
                                        string='Admission status')
