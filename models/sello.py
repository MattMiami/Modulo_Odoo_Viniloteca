from odoo import models, fields, api


class Sello(models.Model):
    _name = 'viniloteca.sello'
    id = fields.Char(string='Id sello', required=True)
    nombre = fields.Char(string='Nombre sello', required=True)
    vinilo = fields.Many2many('viniloteca.vinilo', string='Vinilo')
    pais = fields.Char(string='Pais')
    tienda = fields.Many2many('viniloteca.tienda', string='Tienda')

    def borrar_datos(self):
        self.write({
            'id': '',
            'nombre': '',
            'vinilo': '',
            'pais': ''
        })


    def name_get(self):
        lista = []
        for record in self:
            name = record.nombre
            lista.append((record.id, name))
        return lista

   