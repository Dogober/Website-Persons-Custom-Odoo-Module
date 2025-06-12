from odoo import http
from odoo.http import request

class WebsitePerson(http.Controller):

    @http.route('/persons', auth='public', website=True)
    def list_persons(self, **kwargs):
        persons = request.env['website.person'].sudo().search([], limit=5, order='id desc')
        return request.render('website_persons.template_persons_list', {
            'persons': persons
        })

    @http.route('/persons/add', type='http', auth='public', website=True, methods=['GET', 'POST'])
    def add_person(self, **post):
        if http.request.httprequest.method == 'POST':
            request.env['website.person'].sudo().create({
                'first_name': post.get('first_name'),
                'last_name': post.get('last_name'),
                'birthday': post.get('birthday'),
                'sex': post.get('sex'),
                'company_id': request.env.company.id,
            })
            return request.redirect('/persons')

        return request.render('website_persons.template_add_person', {})
