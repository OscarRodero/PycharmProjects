# -*- coding: utf-8 -*-
from odoo import models, fields, api


class oscar_rodero(models.Model):
    _name = 'modulo_personalizado.oscar_rodero'
    _description = 'modulo_personalizado.oscar_rodero'
    name = fields.Char()
    date = fields.Date()
    description = fields.Char()