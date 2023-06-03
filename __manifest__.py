{
    'name': "Students",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/students_details.xml',
        'views/class_room.xml',
        'views/branches.xml',
        'views/courses.xml',
        'views/batches.xml'

    ],
    'demo': [],
    'summary': "logic_students",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': True
}
