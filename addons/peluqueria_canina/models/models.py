from odoo import models, fields, api
from datetime import datetime


class Mascota(models.Model):
    _name = "peluqueria.mascota"
    _description = "Mascotas"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, help="Introduzca el nombre de la mascota")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    edad = fields.Integer(string="Edad", compute="_compute_edad", store=True)
    raza = fields.Char(string="Raza")
    peso = fields.Float(string="Peso")
    cuidado_especial = fields.Selection(
        string='Cuidado Especial?', default="no",
        selection=[('si', 'Si'), ('no', 'No')]
    )        
    cual = fields.Char(string="¿Cuál?")      
    comportamiento = fields.Text(string="Comportamiento")
    descripcion = fields.Text(string="Descripcion")
    turno_prox = fields.Datetime(string="Proximo Turno")
    image = fields.Binary(string="Imagen")
    owner_id = fields.Many2one('res.partner', string="Dueño", required=True)
    owner_phone = fields.Char(string="Teléfono", related='owner_id.phone', store=False)
    


    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for record in self:
            print(f"Calculando edad para: {record.fecha_nacimiento}")
            if record.fecha_nacimiento:
                today = datetime.today()
                birth_date = fields.Date.from_string(record.fecha_nacimiento)
                edad = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.edad = edad
            else:
                record.edad = 0




class Personas(models.Model):
    _inherit = "res.partner"

    pet_ids = fields.One2many('peluqueria.mascota', 'owner_id', string="Mascotas")   
