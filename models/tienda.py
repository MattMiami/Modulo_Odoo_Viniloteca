from odoo import models, fields, api


class Tienda(models.Model):
    _name = 'viniloteca.tienda'
    id = fields.Char(string='Id Tienda', required=True)
    nombre = fields.Char(string='Nombre tienda', required=True)
    direccion = fields.Char(string='Direccion tienda', required=True)
    telefono = fields.Char(string='Telefono tienda', required=True)
    dependiente = fields.Many2many('viniloteca.dependiente', string='Dependiente')
    sello = fields.Many2many('viniloteca.sello', string='Sello')

    def borrar_datos(self):
        self.write({
            'nombre': '',
            'direccion': '',
            'telefono': '',
            'dependiente': '',
            'sello': ''
        })

    def name_get(self):
        lista = []
        for record in self:
            name = record.nombre
            lista.append((record.id,name))
        return lista