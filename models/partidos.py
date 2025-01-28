

from odoo import models, fields, api


class Partido(models.Model):
    _name = 'futbol_master.partido'
    _description = 'futbol_master.partido'

    equipos = fields.One2many("futbol_master.equipo", string = "Equipos", required = True)
    estadio = fields.Many2many("futbol_master.estadio", string = "Estadio", required = True)
    resultadoLocal = fields.Float(string = "Resultado Local", required = True)
    resultadoVisitante = fields.Float(string = "Resultado Visitante", required = True)
    fecha = fields.Date(string = "Fecha")
    description = fields.Text()

    @api.depends('fecha')
    def _value_pc(self):
        self.fecha = fields.Date.today()
        self.fecha = self.fecha.strftime("%d/%m/%Y")
