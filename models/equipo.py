from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Equipo(models.Model):
    _name = 'futbol_master.equipo'
    _description = 'futbol_master.equipo'

    name = fields.Char(string="Nombre", required=True)
    entrenador_id = fields.Many2one("futbol_master.entrenador", string="Entrenador")
    jugadores = fields.One2many("futbol_master.jugador","equipo_id", string="Jugadores", required=True)
    club_id = fields.Many2one("futbol_master.club", string="Club", required=True)
    division = fields.Selection([("1", "Primera"), ("2", "Segunda"), ("3", "Tercera")], string="Division", required=True)
    partidosGanados = fields.Integer(string="Partidos Ganados", required=True)
    partidosPerdidos = fields.Integer(string="Partidos Perdidos", required=True)
    promedioVictorias = fields.Float(string="Promedio de Victorias",readonly=True, compute="_calcular_promedio",store=True)

    @api.onchange("jugadores")
    def _value_pc(self):
        if len(self.jugadores) > 25:
            raise ValidationError("Has alcanzado el limite de jugadores")

    @api.depends("partidosGanados", "partidosPerdidos")
    def _calcular_promedio(self):
        if self.partidosGanados + self.partidosPerdidos > 0:
            self.promedioVictorias = self.partidosGanados / (self.partidosGanados + self.partidosPerdidos)
        else:
            self.promedioVictorias = 0