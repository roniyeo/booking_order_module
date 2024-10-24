from odoo import models, fields, api

class WorkOrder(models.Model):
    _name = 'work.order'
    _description = 'Work Order'
    _order = 'wo_number'

    wo_number = fields.Char(string='WO Number', required=True, readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('work.order'))
    booking_order_id = fields.Many2one('sale.order', string='Booking Order Reference', readonly=True)
    team_id = fields.Many2one('service.team', string='Team', required=True)
    team_leader_id = fields.Many2one('res.users', string='Team Leader', required=True)
    team_member_ids = fields.Many2many('res.users', string='Team Members')
    planned_start = fields.Datetime(string='Planned Start', required=True)
    planned_end = fields.Datetime(string='Planned End', required=True)
    date_start = fields.Datetime(string='Date Start', readonly=True)
    date_end = fields.Datetime(string='Date End', readonly=True)
    state = fields.Selection([('pending', 'Pending'),
                              ('in_progress', 'In Progress'),
                              ('done', 'Done'),
                              ('cancelled', 'Cancelled')],
                             string='State', default='pending')
    notes = fields.Text(string='Notes')
