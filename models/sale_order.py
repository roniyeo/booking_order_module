from odoo.exceptions import UserError
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string='Is Booking Order')
    team_id = fields.Many2one('service.team', string='Team', ondelete='set null')
    team_leader_id = fields.Many2one('res.users', string='Team Leader')
    team_member_ids = fields.Many2many('res.users', string='Team Members')
    booking_start = fields.Datetime(string='Booking Start')
    booking_end = fields.Datetime(string='Booking End')
    
    def action_check_availability(self):
        overlap_orders = self.env['work.order'].search([
            ('team_id', '=', self.team_id.id),
            ('state', '!=', 'cancelled'),
            ('planned_start', '<=', self.booking_end),
            ('planned_end', '>=', self.booking_start)
        ])
        if overlap_orders:
            overlap_order = overlap_orders[0]
            raise UserError(f"Team already has work order during that period on SO {overlap_order.booking_order_id.name}")
        else:
            self.env.user.notify_info("Team is available for booking")
    
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        for order in self:
            overlap_orders = self.env['work.order'].search([
                ('team_id', '=', order.team_id.id),
                ('state', '!=', 'cancelled'),
                ('planned_start', '<=', order.booking_end),
                ('planned_end', '>=', order.booking_start)
            ])
            if overlap_orders:
                raise UserError(f"Team is not available during this period, already booked on SO{overlap_orders.booking_order_id.name}. Please book on another date.")
            else:
                work_order = self.env['work.order'].create({
                    'booking_order_id': order.id,
                    'team_id': order.team_id.id,
                    'team_leader_id': order.team_leader_id.id,
                    'team_member_ids': [(6, 0, order.team_member_ids.ids)],
                    'planned_start': order.booking_start,
                    'planned_end': order.booking_end,
                    'state': 'pending'
                })
