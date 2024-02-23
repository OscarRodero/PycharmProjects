# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from datetime import datetime

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

    codigo_reserva = fields.Char(compute="_compute_codigo_reserva", string="Código de Reserva", readonly=True)
    fecha_reserva = fields.Datetime(string="Fecha de Reserva", required=True)
    numero_horas = fields.Selection([("1", '1 hora'),("2", '2 horas'),("3", '3 horas')], string="Número de Horas", required=True)
    fecha_fin_reserva = fields.Datetime(string="Fecha de Fin de Reserva", compute="_compute_fecha_fin_reserva", store=True)
    grupo_de_trabajo = fields.Many2one('reservas.grupo', string="Grupo de Trabajo", required=True)
    sala_de_reuniones = fields.Many2one('reservas.sala', string="Sala de Reuniones", compute="_compute_sala_de_reuniones", store=True)

    @api.depends('grupo_de_trabajo', 'fecha_reserva')
    def _compute_codigo_reserva(self):
        for n in self:
            if (n.grupo_de_trabajo and n.fecha_reserva):
                nombre_grupo = n.grupo_de_trabajo.nombre if n.grupo_de_trabajo else ''
                fecha_formateada = n.fecha_reserva.strftime('%d/%m/%Y_%H:%M:%S')
                n.codigo_reserva = "RES_" + nombre_grupo + "_" + fecha_formateada
            else:
                n.codigo_reserva = ''

    @api.depends('fecha_reserva', 'numero_horas')
    def _compute_fecha_fin_reserva(self):
        for reserva in self:
            if reserva.fecha_reserva and reserva.numero_horas:
                reserva.fecha_fin_reserva = reserva.fecha_reserva + relativedelta(hours=int(reserva.numero_horas))

    @api.depends('fecha_reserva', 'grupo_de_trabajo')
    def _compute_sala_de_reuniones(self):
        for reserva in self:
            if reserva.fecha_reserva and reserva.grupo_de_trabajo:
                salas_disponibles = self.env['reservas.sala'].search([('capacidad', '>=', reserva.grupo_de_trabajo.numero_integrantes)])
                if salas_disponibles:
                    reserva.sala_de_reuniones = salas_disponibles[0].id


