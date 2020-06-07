# -*- coding: utf-8 -*-

from odoo import fields, models

class TaskSchedular(models.Model):
    _name='task.schedular'
    _description='Task Schedular'
	
    name=fields.Char('Task name')
    user_id = fields.Many2one(
        'res.users', string='Responsible', index=True, required=True,
         default=lambda self: self.env.user)
    description=fields.Text('Task descrition')
    start_date = fields.Date('Start Date', index=True)
    expiry_date = fields.Date('Expiry Date', index=True)
	
