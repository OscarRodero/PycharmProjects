# -*- coding: utf-8 -*-
# from odoo import http


# class Tareas(http.Controller):
#     @http.route('/tareas/tareas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tareas/tareas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tareas.listing', {
#             'root': '/tareas/tareas',
#             'objects': http.request.env['tareas.tareas'].search([]),
#         })

#     @http.route('/tareas/tareas/objects/<model("tareas.tareas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tareas.object', {
#             'object': obj
#         })
