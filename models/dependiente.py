from odoo import models, fields, api


class Dependiente(models.Model):
    _name = 'viniloteca.dependiente'
    id = fields.Char(string='Id Dependiente', required=True)
    dni = fields.Char(string='Dni', required=True)
    nombre = fields.Char(string='Nombre dependiente', required=True)
    apellidos = fields.Char(string='Apellidos dependiente')
    fecha = fields.Date(string="Fecha de Venta")
    comprador = fields.Many2many('viniloteca.comprador', string='Comprador')
    tienda = fields.Many2many('viniloteca.tienda', string='Tienda')
   

    def borrar_datos(self):
        self.write({
            'dni': '',
            'nombre': '',
            'apellidos': '',
            'fecha': '',
            'comprador': '',
            'tienda': ''


        })

    def name_get(self):
        lista = []
        for record in self:
            name = record.nombre
            lista.append((record.id,name))
        return lista