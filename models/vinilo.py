from odoo import models, fields, api


class Vinilo(models.Model):
    _name = 'viniloteca.vinilo'
    id = fields.Char(string='Id Vinilo', required=True)
    nombre = fields.Char(string='Nombre Vinilo', required=True)
    genero = fields.Char(string='Genero', required=True)
    fecha = fields.Date(string='Fecha lanzamiento', required=True)
    sello = fields.Many2many('viniloteca.sello', string='Sello')
    precio = fields.Integer(string='Precio', required=True)

    def borrar_datos(self):
        self.write({
            'id': '',
            'nombre': '',
            'genero': '',
            'fecha': '',
            'precio': ''
        })


    def name_get(self):
        lista = []
        for record in self:
            name = record.nombre
            lista.append((record.id, name))
        return lista

