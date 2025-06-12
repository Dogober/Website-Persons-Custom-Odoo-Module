# noinspection PyStatementEffect
{
    'name': 'Website Persons',
    'version': '16.0.1.0.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/person_views.xml',
        'templates/website_person_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_persons/static/src/css/website_persons.css',
        ],
    },
    'application': True,
}
