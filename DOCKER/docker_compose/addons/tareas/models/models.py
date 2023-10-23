# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'Modelo de Tareas'

    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la tarea')
    descripcion = fields.Text(string='Descripción')
    horas = fields.Float(string='Horas')
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)
    fecha_comienzo = fields.Datetime(string='Fecha de Comienzo')
    fecha_fin = fields.Datetime(string='Fecha de Fin')
    pausada = fields.Boolean(string='Pausada', default=False)
    sprint = fields.Many2one('tareas.sprint', string='Sprint')
    tecnologias = fields.Many2many('tareas.tecnologias', string='Tecnologías')

class Sprint(models.Model):
    _name = 'tareas.sprint'
    _description = 'Modelo de Sprint'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_creacion = fields.Datetime(string='Fecha de Creación', default=fields.Datetime.now)
    fecha_fin = fields.Datetime(string='Fecha de Fin')
    tareas = fields.One2many('tareas.tareas', 'sprint', string='Tareas')

class Tecnologias(models.Model):
    _name = 'tareas.tecnologias'
    _description = 'Modelo de Tecnologías'

    nombre = fields.Char(string='Nombre', required=True)
    imagen = fields.Image(string='Imagen', maxwidth=200, maxheight=200)
    tareas = fields.Many2many('tareas.tareas', string="Tareas")
