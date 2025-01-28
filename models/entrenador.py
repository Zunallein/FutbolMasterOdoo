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
    calificacion_promedio = fields.Integer(string="Calificación promedio", readonly=True)

    @api.depends('equipos')
    def _calcular_promedio(self):
        total_partidos = self.partidos_ganados + self.partidos_perdidos
        partidos_ganados = self.partidos_ganados

        if total_partidos > 0:
            self.calificacion_promedio = (partidos_ganados / total_partidos) * 100
        else:
            self.calificacion_promedio = 0