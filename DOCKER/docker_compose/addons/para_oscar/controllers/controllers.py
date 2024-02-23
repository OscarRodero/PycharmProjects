# -*- coding: utf-8 -*-
# from odoo import http


# class ParaOscar(http.Controller):
#     @http.route('/para_oscar/para_oscar', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/para_oscar/para_oscar/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('para_oscar.listing', {
#             'root': '/para_oscar/para_oscar',
#             'objects': http.request.env['para_oscar.para_oscar'].search([]),
#         })

#     @http.route('/para_oscar/para_oscar/objects/<model("para_oscar.para_oscar"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('para_oscar.object', {
#             'object': obj
#         })
