# -*- coding: utf-8 -*-

from odoo import models, fields, api


class matadero(models.Model):
    _name = 'matadero.matadero'     
    _description = 'matadero.matadero'

    nombre = fields.Char()
    duracion = fields.Integer()
    fecha_fin = fields.Datetime(compute="_value_pc", store=True)
    fecha_inicial = fields.Datetime()

    @api.depends("fecha_inicial", "duracion")
    def _calcula_fecha_fin(self):
        for muerto in self:
            if(muerto.duracion > 0):
                muerto.fecha_fin = muerto.fecha_inicial + timedelta(days=muerto.duracion)
            else:
                muerto.fecha_fin = muerto.fecha_inicial