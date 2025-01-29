from odoo import models, fields, api
from datetime import datetime

class Partido(models.Model):
    _name = 'futbol_master.partido'
    _description = 'futbol_master.partido'

    equipos = fields.Many2many("futbol_master.equipo", string = "Equipos", required = True)
    nombreLocal = fields.Char(string = "Nombre Local")
    nombreVisitante = fields.Char(string = "Nombre Visitante")
    estadio = fields.Many2many("futbol_master.estadio", string = "Estadio", required = True)
    resultadoLocal = fields.Integer(string = "Resultado Local")
    resultadoVisitante = fields.Integer(string = "Resultado Visitante")
    fecha = fields.Date(string = "Fecha", default=datetime.today())

    @api.constrains('resultadoLocal', 'resultadoVisitante')
    def _value_pc(self):
        if len(self.equipos) < 2:
            raise models.ValidationError('Tiene que haber al menos 2 equipos para poder jugar un partido')
        self.nombreLocal = self.equipos[0].name
        self.nombreVisitante = self.equipos[1].name

    @api.onchange('equipos')
    def _max_eqipos(self):
        if len(self.equipos) > 2:
            raise models.ValidationError('Solo se pueden seleccionar 2 equipos')
        
    @api.onchange('estadio')
    def _max_estadio(self):
        if len(self.estadio) > 1:
            raise models.ValidationError('Solo se puede seleccionar 1 estadio')
        
        

    @api.constrains('resultadoLocal', 'resultadoVisitante')
    def _jugarPartido(self):
        #nada todavia
        pass