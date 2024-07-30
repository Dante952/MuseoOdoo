{
    'name': 'Art Gallery',
    'version': '1.0',
    'summary': 'Module to manage art gallery inventory',
    'sequence': -100,
    'description': """Module to manage art gallery inventory including title, description, author, image URL, audio URL, and price.""",
    'category': 'Inventory',
    'author': 'Your Name',
    'maintainer': 'Your Name',
    'website': 'http://yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/art_piece_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
