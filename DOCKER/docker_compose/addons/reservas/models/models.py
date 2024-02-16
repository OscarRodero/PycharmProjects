# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class sala(models.Model):
    _name = 'reservas.sala'
    _description = 'reservas.sala'

    nombre = fields.Char(string="Nombre", required=True)
    capacidad = fields.Integer(string="Capacidad", required=True)
    reservas_ids = fields.One2many('reservas.reserva', 'sala_de_reuniones', string="Reservas")

class grupo(models.Model):
    _name = 'reservas.grupo'
    _description = 'reservas.grupo'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción", required=False)
    numero_integrantes = fields.Integer(string="Número de Integrantes", required=True)
    reserva_id = fields.Many2one('reservas.reserva', string="Reserva")

class reservas(models.Model):
    _name = 'reservas.reserva'
    _description = 'reservas.reserva'    

    codigo_reserva = fields.Char(string="Código de Reserva", store=True)
    fecha_reserva = fields.Date(string="Fecha de Reserva", required=True)
    numero_horas = fields.Selection([(1, '1 hora'),(2, '2 horas'),(3, '3 horas')], string="Número de Horas", required=True)
    fecha_fin_reserva = fields.Date(string="Fecha de Fin de Reserva", store=True)
    grupo_de_trabajo = fields.Many2one('reservas.grupo', string="Grupo de Trabajo", required=True)
    sala_de_reuniones = fields.Many2one('reservas.sala', string="Sala de Reuniones", required=True)

