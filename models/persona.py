# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'futbol_master.persona'
    _description = 'Persona'

    name = fields.Char(string="Nombre",required=True)
    edad = fields.Integer(string="Edad", required=True)
    genero = fields.Selection([ ("1","Masculino"), ("2","Femenino")],string="Genero",required=True)
    pais = fields.Many2one('res.country', string="País",required=True)

    @api.onchange('edad')
    def comprobar_edad(self):
        if self.edad < 16:
            self.edad = 16
        elif self.edad > 100:
            self.edad = 100