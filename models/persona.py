# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persona(models.Model):
    _name = 'futbol_master.persona'
    _description = 'Persona'

    nombre = fields.Char(string="Nombre")
    edad = fields.Integer(string="Edad")
    genero = fields.Selection(["Masculino", "Femenino"],string="Genero")
    pais = fields.Char(string="País")

