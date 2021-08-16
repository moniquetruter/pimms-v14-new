{
    'name': 'Pimms Group: Divisions',
    'version': '14.0.1.0.0',
    'author': 'SystemWorks',
    'website': 'https://www.systemworks.co.za',
    'category': 'Custom',
    'summary': 'Company Divisions for Pimms Group',
    'depends': [
        'base',
        'account',
    ],
    'data': [
        'views/account_views.xml',
        'views/division_views.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'OPL-1',
    'installable': True,
    'application': False,
}
