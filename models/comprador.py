from odoo import models, fields, api


class Comprador(models.Model):
    _name = 'viniloteca.comprador'
    id = fields.Char(string='Id Comprador', required=True)
    dni = fields.Char(string='Dni', required=True)
    nombre = fields.Char(string='Nombre del comprador', required=True)
    apellidos = fields.Char(string='Apellidos del comprador', required=True)
    telefono = fields.Char(string='Telefono del comprador')
    direccion = fields.Char(string='Direccion del comprador')
    dependiente = fields.Many2many('viniloteca.dependiente', string='Dependiente')

    def borrar_datos(self):
        self.write({
            'dni': '',
            'nombre': '',
            'apellidos': '',
            'telefono': '',
            'direccion': ''
        })

    def name_get(self):
        lista = []
        for record in self:
            name = record.nombre
            lista.append((record.id, name))
        return lista