# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Entrenador(models.Model):
    _inherit = 'futbol_master.persona'

    _name = 'futbol_master.entrenador'
    _description = 'Entrenador'

    #equipos = fields.Many2one(comodel_name="futbol_master.equipo",string="Equipos")
    anio_experiencia = fields.Integer(string="Años de experiencia")
    calificacion_promedio = fields.Integer(string="Calificación promedio")
