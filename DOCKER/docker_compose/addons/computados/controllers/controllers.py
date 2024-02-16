# -*- coding: utf-8 -*-
# from odoo import http


# class Computados(http.Controller):
#     @http.route('/computados/computados', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/computados/computados/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('computados.listing', {
#             'root': '/computados/computados',
#             'objects': http.request.env['computados.computados'].search([]),
#         })

#     @http.route('/computados/computados/objects/<model("computados.computados"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('computados.object', {
#             'object': obj
#         })
