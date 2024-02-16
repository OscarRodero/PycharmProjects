# -*- coding: utf-8 -*-

from odoo import models, fields, api


class computados(models.Model):
    _name = 'computados.computados'
    _description = 'computados.computados'

    num1 = fields.Integer()
    num2 = fields.Integer()
    res = fields.Integer(compute='_compute_result', store=True)

    @api.depends('num1', 'num2')
    def _compute_result(self):
        for record in self:
            record.res = record.num1 + record.num2