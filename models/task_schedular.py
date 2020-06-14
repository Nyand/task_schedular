# -*- coding: utf-8 -*-


from odoo import fields, models

from odoo.exceptions import UserError

class TaskSchedular(models.Model):
    _name='task.schedular'
    _description='Task Schedular'
    _inherit = ['mail.thread','mail.activity.mixin']
    _order = 'expiry_date ASC'
	
    name=fields.Char('Task name', required=True)
    user_id = fields.Many2one(
        'res.users', string='Responsible', index=True, required=True,
         default=lambda self: self.env.user)
    description=fields.Text('Task description')
    start_date = fields.Date('Start Date', index=True, required=True)
    expiry_date = fields.Date('Expiry Date', index=True, required=True, track_visibility='onchange')
    state=fields.Selection([("new", "New"),
	    ("in_progress", "In Progress"),
	    ("completed", "Completed"),
	    ("expired", "Expired")],
	    default='new', track_visibility='onchange', index=True, group_expand="_expand_states")
    last_modification = fields.Datetime(readonly=True)
	
	
    _sql_constraints = [('project_date_greater', 'check(expiry_date >= start_date)', 'Error! project start-date must be lower than project expiry_date')]

	
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]


    def write(self, values):
        # help to "YYY-MM-DD"
        values['last_modification']=fields.Datetime.now()
        return super(TaskSchedular, self).write(values)		

    def unlink(self):
	    for task in self:
		    if task.state =='completed':
			    raise UserError("You can not delete completed tasks")
        
