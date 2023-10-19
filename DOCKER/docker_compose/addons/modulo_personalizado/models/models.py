# -*- coding: utf-8 -*-
from odoo import models, fields, api

class modulo_personalizado(models.Model):
    _name = 'modulo_personalizado.modulo_personalizado'
    _description = 'modulo_personalizado.modulo_personalizado'
    name = fields.Char()

class oscar_rodero(models.Model):
    _name = 'modulo_personalizado.oscar_rodero'
    _description = 'modulo_personalizado.oscar_rodero'
    name = fields.Char()