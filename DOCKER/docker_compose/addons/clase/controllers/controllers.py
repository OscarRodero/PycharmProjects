# -*- coding: utf-8 -*-
# from odoo import http


# class Clase(http.Controller):
#     @http.route('/clase/clase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clase/clase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clase.listing', {
#             'root': '/clase/clase',
#             'objects': http.request.env['clase.clase'].search([]),
#         })

#     @http.route('/clase/clase/objects/<model("clase.clase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clase.object', {
#             'object': obj
#         })
