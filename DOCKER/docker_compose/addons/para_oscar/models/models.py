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

class Almacen(models.Model):
    _name = 'para_oscar.almacen' 
    _description = 'para_oscar.almacen'

    name = fields.Char(string="Nombre", required=True)
    location = fields.Char(string="Ubicación", required=True)
    opening_time = fields.Float(string="Hora de Apertura", required=True)
    closing_time = fields.Float(string="Hora de Cierre", required=True)
    estanterias_ids = fields.One2many('para_oscar.estanteria', 'almacen_id', string="Estanterías")

class Estanteria(models.Model):
    _name = 'para_oscar.estanteria'
    _description = 'para_oscar.estanteria'

    codigo = fields.Integer(string="Código", required=True, readonly=True, copy=False, default=lambda self: self._get_next_code())
    almacen_id = fields.Many2one('para_oscar.almacen', string="Almacén", required=True)
    lote_id = fields.Many2one('para_oscar.lote', string="Lote")
    m3 = fields.Float(string="Metros Cúbicos", required=True)

    def _get_next_code(self):
        last_record = self.search([], order='codigo desc', limit=1)
        if last_record:
            return last_record.codigo + 1
        else:
            return 1

class Entrega(models.Model):
    _name = 'para_oscar.entrega'
    _description = 'para_oscar.entrega'

    fecha_hora_entrega = fields.Datetime(string="Fecha y Hora de Entrega", required=True, default=lambda self: fields.Datetime.now())
    almacen_id = fields.Many2one('para_oscar.almacen', string="Almacén de Entrega", required=True)
    estanteria_id = fields.Many2one('para_oscar.estanteria', string="Estantería", required=True)
    lote_id = fields.Many2one('para_oscar.lote', string="Lote Entregado", required=True)

    @api.onchange('fecha_hora_entrega')
    def _onchange_fecha_hora_entrega(self):
        almacen_disponible = self.env['para_oscar.almacen'].search([('opening_time', '<=', self.fecha_hora_entrega.hour), ('closing_time', '>=', self.fecha_hora_entrega.hour)])
        if not almacen_disponible:
            self.almacen_id = False
        else:
            self.almacen_id = almacen_disponible[0].id

    @api.onchange('almacen_id')
    def _onchange_almacen_id(self):
        if self.almacen_id:
            estanterias_disponibles = self.env['para_oscar.estanteria'].search([('almacen_id', '=', self.almacen_id.id), ('lote_id', '=', False)])
            if estanterias_disponibles:
                self.estanteria_id = estanterias_disponibles[0].id
            else:
                self.estanteria_id = False

class Lote(models.Model):
    _name = 'para_oscar.lote'
    _description = 'para_oscar.lote'

    number = fields.Integer(string="Número de lote", required=True, readonly=True, copy=False, default=lambda self: self._get_next_number())
    code = fields.Char(string="Código del lote", compute='_compute_code', store=True)
    product_id = fields.Many2one('para_oscar.producto', string="Producto", required=True)
    quantity = fields.Integer(string="Cantidad", required=True)
    type = fields.Selection([("1", 'Rectangular'), ("2", 'Cuadrado')], string="Tipo", required=True)
    m3 = fields.Float(string="Metros Cúbicos", compute='_compute_m3', store=True)

    estanteria_id = fields.Many2one('para_oscar.estanteria', string="Estantería")

    def _get_next_number(self):
        last_record = self.search([], order='number desc', limit=1)
        if last_record:
            return last_record.number + 1
        else:
            return 1

    @api.depends('number')
    def _compute_code(self):
        for record in self:
            record.code = f"COD-{record.number:04d}"

    @api.depends('quantity', 'type')
    def _compute_m3(self):
        for record in self:
            if record.type == '1':
                record.m3 = record.quantity * 2.5
            elif record.type == '2':
                record.m3 = record.quantity * 1.5 