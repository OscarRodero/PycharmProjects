# -*- coding: utf-8 -*-
# from odoo import http


# class Pedidos3d(http.Controller):
#     @http.route('/pedidos_3d/pedidos_3d', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pedidos_3d/pedidos_3d/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pedidos_3d.listing', {
#             'root': '/pedidos_3d/pedidos_3d',
#             'objects': http.request.env['pedidos_3d.pedidos_3d'].search([]),
#         })

#     @http.route('/pedidos_3d/pedidos_3d/objects/<model("pedidos_3d.pedidos_3d"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pedidos_3d.object', {
#             'object': obj
#         })
