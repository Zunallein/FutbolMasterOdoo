from odoo import models, fields, api


class Estadio(models.Model):
    _name = 'futbol_master.estadio'
    _description = 'futbol_master.estadio'

    name = fields.Char()
    ubicacion = fields.Char(string="Ubicacion", required=True)
    capacidad = fields.Integer(string="Capacidad", required=True)


