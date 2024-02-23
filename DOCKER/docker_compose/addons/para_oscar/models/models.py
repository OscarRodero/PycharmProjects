from datetime import datetime, timedelta
from odoo import models, fields, api

class Producto(models.Model):
    _name = 'para_oscar.producto' 
    _description = 'para_oscar.producto'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción", required=False)
    price = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock", required=True)
    caducity = fields.Date(string="Caducidad", required=False)
    category_id = fields.Many2one('para_oscar.categoria', string="Categoría", required=True)
    image = fields.Binary(string="Imagen", required=False)
    expiration_criticality = fields.Selection([("1", 'Baja'), ("2", 'Media'), ("3", 'Alta')], string="Criticidad de Caducidad", compute='_compute_expiration_criticality', store=True)
    product_code = fields.Char(string="Código de Producto", compute='_compute_product_code', store=True)
    category = fields.Char(string="Categoría", compute='_compute_category', store=True)

    @api.depends('caducity')
    def _compute_expiration_criticality(self):
        for record in self:
            if record.caducity:
                expiration_date = fields.Date.from_string(record.caducity)
                today = datetime.now().date()
                days_remaining = (expiration_date - today).days
                if days_remaining < 10:
                    record.expiration_criticality = '3'  # Alta
                elif 10 <= days_remaining <= 40:
                    record.expiration_criticality = '2'  # Media
                else:
                    record.expiration_criticality = '1'  # Baja

    @api.depends('category_id')
    def _compute_category(self):
        for record in self:
            if record.category_id:
                record.category = record.category_id.name

    @api.depends('name', 'category_id')
    def _compute_product_code(self):
        for record in self:
            if record.name and record.category_id:
                record.product_code = f"{record.name}_{record.category_id.code}"


class Categoria(models.Model):
    _name = 'para_oscar.categoria'
    _description = 'para_oscar.categoria'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción", required=False)
    code = fields.Char(string="Código", compute='_compute_category_code', store=True)
    products = fields.One2many('para_oscar.producto', 'category_id', string="Productos")

    @api.depends('name')
    def _compute_category_code(self):
        for category in self:
            if category.name:
                words = category.name.split()
                code_parts = [word[:3].upper() for word in words]
                category.code = '-'.join(code_parts[:3])