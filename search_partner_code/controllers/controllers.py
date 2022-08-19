# -*- coding: utf-8 -*-
# from odoo import http


# class SearchPartnerCode(http.Controller):
#     @http.route('/search_partner_code/search_partner_code', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/search_partner_code/search_partner_code/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('search_partner_code.listing', {
#             'root': '/search_partner_code/search_partner_code',
#             'objects': http.request.env['search_partner_code.search_partner_code'].search([]),
#         })

#     @http.route('/search_partner_code/search_partner_code/objects/<model("search_partner_code.search_partner_code"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('search_partner_code.object', {
#             'object': obj
#         })
