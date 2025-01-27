from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Equipo(models.Model):
    _name = 'futbol_master.equipo'
    _description = 'futbol_master.equipo'

    name = fields.Char(string = "Nombre", required = True)
    entrenador = fields.Many2many("futbol_master.entrenador", string = "Entrenador", required = True)
    jugador = fields.Many2one("futbol_master.entrenador", string = "Jugadores", required = True)
    division = fields.Selection([("1", "Primera"), ("2", "Segunda"), ("3", "Tercera")], string = "Division", required = True)
    partidosGanados = fields.Integer(string = "Partidos Ganados", required = True)
    partidosPerdidos = fields.Integer(string = "Partidos Perdidos", required = True)
    promedioVictorias = fields.Float(string = "Promedio de Victorias")

    @api.onchange("jugador")
    def _value_pc(self):
        if self.jugador.size() > 25:
            raise ValidationError("Has alcanzado el limite de jugadores")

    @api.onchange("partidosGanados", "partidosPerdidos")
    def _value_pc(self):
        self.promedioVictorias = self.partidosGanados / (self.partidosGanados + self.partidosPerdidos)