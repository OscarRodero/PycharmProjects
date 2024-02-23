# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clase(models.Model):
     _name = 'clase.clase'
     _description = 'clase.clase'

     nombre = fields.Char()
     description = fields.Char()
     alumnos = fields.One2many("clase.alumno", 'clase')
     #modulo = fields.Many2one("clase.modulo")
#     value2 = fields.Float(compute="_value_pc", store=True)
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class alumno(models.Model):
     _name = 'clase.alumno'
     _description = 'clase.alumno'

     nombre = fields.Char()
     apellido1 = fields.Char()
     apellido2 = fields.Char()
     nombreCompleto = fields.Char(compute="_NombreCompleto", store=True)
     clase = fields.Many2one("clase.clase")
     
     @api.depends('nombre','apellido1','apellido2')
     def _NombreCompleto(self):
         for n in self:
             if(n.nombre and n.apellido1 and n.apellido2):
                n.nombreCompleto = n.nombre + ' '+n.apellido1 + ' '+n.apellido2
             else:
                 n.nombreCompleto = ''

class modulo(models.Model):
     _name = 'clase.modulo'
     _description = 'clase.modulo'

     nombre = fields.Char()
     description = fields.Char()
     #clases = fields.One2many("clase.clase", 'modulo')       