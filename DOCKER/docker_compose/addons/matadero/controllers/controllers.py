# -*- coding: utf-8 -*-
# from odoo import http


# class Matadero(http.Controller):
#     @http.route('/matadero/matadero', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/matadero/matadero/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('matadero.listing', {
#             'root': '/matadero/matadero',
#             'objects': http.request.env['matadero.matadero'].search([]),
#         })

#     @http.route('/matadero/matadero/objects/<model("matadero.matadero"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('matadero.object', {
#             'object': obj
#         })
