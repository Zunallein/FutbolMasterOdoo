# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Jugador(models.Model):
    _inherit = 'futbol_master.persona'

    _name = 'futbol_master.jugador'
    _description = 'futbol_master.futbol_master'
    
    posicion = fields.Selection(["Portero", "Defensa", "Medio", "Delantero"],string="Posición")
    numero = fields.Integer(string="Numero del jugador")
    seleccion = fields.Boolean(string="¿Pertenece a la selección?")

@api.onchange('numero')
def comprobar_numero(self):
    if self.numero < 0:
        self.numero = 1
    elif self.numero > 99:
        self.numero = 1