# -*- coding: utf-8 -*-

from odoo.http import request, Controller, route
class WebFormController(Controller):
    @route('/airtite_form', auth='public', website=True)
    def web_form(self, **kwargs):
        return request.render('airtite_form.web_form_template')
    @route('/airtite_form/submit', type='http', auth='public', website=True, methods=['POST'])
    def web_form_submit(self, **post):
        request.env['custom.web.form.airtite_form'].sudo().create({
                    'name': post.get('name'),
                    'phone': post.get('phone'),
                    'email': post.get('email'),
                })
        return request.redirect('/thank-you-page')
