from odoo.exceptions import UserError
from odoo import models, fields

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Service Team'

    name = fields.Char(string='Team Name', required=True)
    team_leader_id = fields.Many2one('res.users', string='Team Leader', required=True)
    team_member_ids = fields.Many2many('res.users', string='Team Members')
    active = fields.Boolean(string='Active', default=True)
    
    def unlink(self):
        for team in self:
            sales_orders = self.env['sale.order'].search([('team_id', '=', team.id)])
            if sales_orders:
                raise UserError(f"Cannot delete team {team.name} because it is referenced in Sales Orders.")
        return super(ServiceTeam, self).unlink()
