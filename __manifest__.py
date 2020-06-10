# -*- coding: utf-8 -*-
{
    'name': 'Task Schedular',
    'author': 'Robert Mauti',
    'depends': ['base', 'mail'],
    'version': '1.0',
    'description': """
	a task scheduling app
""",
    'auto_install': False,
    'demo': [],
    'data': [
		'security/ir.model.access.csv',
		'views/task_schedular_views.xml'
		
	],
    'installable': True,
    'application': True,
}
