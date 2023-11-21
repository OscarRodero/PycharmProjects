# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedidos(models.Model):
    _name = 'pedidos_3d.pedidos'
    _description = 'pedidos_3d.pedidos'
    
    id_pedido = fields.Integer(string='ID del Pedido', default=lambda self: self.env['ir.sequence'].next_by_code('pedidos_3d.sequence'))
    id_cliente = fields.Many2one('res.partner', string='ID del cliente')
    email_cliente = fields.Char(related='id_cliente.email', string='Email del Cliente', readonly=True)
    dimensiones = fields.Char(string='Dimensiones', help='Formato: Ancho x Alto x Profundidad')
    archivos_adjuntos = fields.Many2many('ir.attachment', string='Archivos Adjuntos')
