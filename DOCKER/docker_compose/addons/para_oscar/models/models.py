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
    tags = fields.Many2many('para_oscar.etiqueta', string="Etiquetas")

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

class Etiqueta(models.Model):
    _name = 'para_oscar.etiqueta'
    _description = 'para_oscar.etiqueta'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción", required=False)
    products = fields.Many2many('para_oscar.producto', string="Productos")

class Lote(models.Model):
    _name = 'para_oscar.lote'
    _description = 'para_oscar.lote'

    number = fields.Char(string="Número", required=True)
    code = fields.Char(string="Código", required=True)
    product = fields.Many2one('para_oscar.producto', string="Producto", required=True)
    quantity = fields.Integer(string="Cantidad", required=True)
    type = fields.Selection([("1", 'Rectangular'), ("2", 'Cuadrado')], string="Tipo", required=True)
    m3 = fields.Float(string="Metros Cúbicos", compute='_compute_m3', store=True)

    @api.constrains('number')
    def _check_number_length(self):
        for lote in self:
            if lote.number and len(lote.number) != 4:
                raise ValidationError("El número de lote debe tener exactamente 4 caracteres.")
            
    @api.depends('number')
    def _compute_code(self):
        for lote in self:
            lote.code = "COD-" + lote.number

class Entrega(models.Model):
    _name = 'para_oscar.entrega'
    _description = 'Entrega'

    deliver_date = fields.Datetime(string="Fecha y Hora de Entrega", required=True)
    storage_id = fields.Many2one('para_oscar.almacen', string="Almacén de Entrega", required=True)

class Estanteria(models.Model):
    _name = 'para_oscar.estanteria'
    _description = 'Estantería'

    name = fields.Char(string="Nombre", required=True)
    storage_id = fields.Many2one('para_oscar.almacen', string="Almacén", required=True)
    product_id = fields.Many2one('para_oscar.producto', string="Producto")

class Almacen(models.Model):
    _name = 'para_oscar.almacen'
    _description = 'Almacén'

    name = fields.Char(string="Nombre", required=True)
    shelves_ids = fields.One2many('para_oscar.estanteria', 'almacen_id', string="Estanterías")