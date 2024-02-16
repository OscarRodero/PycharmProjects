# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)
class Tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'Modelo de Tareas'

    idTarea = fields.Integer(string='ID', required=True, help='ID de la tarea', compute='_compute_id', store=True)
    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la tarea', compute='_compute_nombre', store=True)
    sprint_id = fields.Many2one('tareas.sprint', string='Sprint asociado', help='Sprint asociado a la tarea')

    @api.depends('idTarea')
    def _compute_id(self):
        for record in self:
            if not record.idTarea:
                last_tarea = self.search([], order='idTarea desc', limit=1)
                record.idTarea = last_tarea.idTarea + 1 if last_tarea else 1

    @api.depends('sprint_id', 'idTarea')
    def _compute_nombre(self):
        for record in self:
            sprint_name = record.sprint_id.nombre if record.sprint_id else ''
            record.nombre = f'{sprint_name}_task_{record.idTarea}' if sprint_name else f'task_{record.idTarea}'


class Sprint(models.Model):
    _name = 'tareas.sprint'
    _description = 'Modelo de Sprint'

    nombre = fields.Char(string='Nombre', required=True, help='Nombre del sprint')
    fechaInicio = fields.Date(string='Fecha de Inicio', required=True, help='Fecha de inicio del sprint')
    duracion = fields.Integer(string='Duración', required=True, help='Duración del sprint en días', compute='_compute_duracion', store=True)
    fechaFin = fields.Date(string='Fecha de Fin', compute='_calcular_fecha_fin', store=True)
    proyecto_id = fields.Many2one('tareas.proyecto', string='Proyecto asociado', help='Proyecto asociado al sprint')
    tareas = fields.One2many('tareas.tareas', 'sprint_id', string='Tareas', help='Tareas asociadas al sprint')

    @api.depends('fechaInicio', 'duracion')
    def _calcular_fecha_fin(self):
        for record in self:
            record.fechaFin = record.fechaInicio + timedelta(days=record.duracion)

    @api.depends('fechaInicio')
    def _comprobar_dia():
        for record in self:
            if record.fechaInicio < datetime.now().date():
                _logger.error('ValueError: No se permite que el día sea menor que el de hoy')
                raise ValueError('No se permite que el día sea menor que el de hoy')
            
class HistoriaUsuario(models.Model):
    _name = 'tareas.historia_usuario'
    _description = 'Modelo de Historia de Usuario'

    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la historia de usuario')
    descripcion = fields.Text(string='Descripción', help='Descripción de la historia de usuario')
    tareas = fields.One2many('tareas.tareas', 'historia_usuario_id', string='Tareas', help='Tareas asociadas a la historia de usuario')
            
class Proyecto(models.Model):
    _name = 'tareas.proyecto'
    _description = 'Modelo de Proyecto'

    nombre = fields.Char(string='Nombre', required=True, help='Nombre del proyecto')
    descripcion = fields.Text(string='Descripción', help='Descripción del proyecto')
    sprints = fields.One2many('tareas.sprint', 'proyecto_id', string='Sprints', help='Sprints asociados al proyecto')