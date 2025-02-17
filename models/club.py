from odoo import models, fields, api
from datetime import datetime


class Club(models.Model):
    _name = 'futbol_master.club'
    _description = 'futbol_master.club'

    name = fields.Char()
    equipo_id = fields.One2many("futbol_master.equipo", "club_id", string="Equipos")
    fechaCreacion = fields.Date(string="Fecha de Creacion", readonly=True, default=datetime.today())
