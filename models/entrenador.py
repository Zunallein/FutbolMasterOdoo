# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Entrenador(models.Model):
    _inherit = 'futbol_master.persona'

    _name = 'futbol_master.entrenador'
    _description = 'Entrenador'

    equipos = fields.One2many(comodel_name="futbol_master.equipo", inverse_name="entrenador_id", string="Equipos")
    anio_experiencia = fields.Integer(string="Años de experiencia")
    partidos_ganados = fields.Integer(string="Partidos ganados")
    partidos_perdidos = fields.Integer(string="Partidos perdidos")
    calificacion_promedio = fields.Float(string="Calificación promedio", readonly=True)

    @api.onchange('partidos_ganados','partidos_perdidos')
    def _calcular_promedio(self):
        if self.partidos_ganados + self.partidos_perdidos > 0:
            self.calificacion_promedio = self.partidos_ganados / (self.partidos_ganados + self.partidos_perdidos)
        else:
            self.calificacion_promedio = 0


