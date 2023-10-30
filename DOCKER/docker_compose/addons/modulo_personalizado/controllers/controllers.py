# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloPersonalizado(http.Controller):
#     @http.route('/modulo_personalizado/modulo_personalizado', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_personalizado/modulo_personalizado/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_personalizado.listing', {
#             'root': '/modulo_personalizado/modulo_personalizado',
#             'objects': http.request.env['modulo_personalizado.modulo_personalizado'].search([]),
#         })

#     @http.route('/modulo_personalizado/modulo_personalizado/objects/<model("modulo_personalizado.modulo_personalizado"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_personalizado.object', {
#             'object': obj
#         })
