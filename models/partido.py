from odoo import models, fields, api
from datetime import datetime
import random

class Partido(models.Model):
    _name = 'futbol_master.partido'
    _description = 'futbol_master.partido'

    equipos = fields.Many2many("futbol_master.equipo", string="Equipos", required=True)
    nombreLocal = fields.Char(string="Nombre Local")
    nombreVisitante = fields.Char(string="Nombre Visitante")
    estadio = fields.Many2many("futbol_master.estadio", string="Estadio", required=True)
    resultadoLocal = fields.Integer(string="Resultado Local", default=0)
    resultadoVisitante = fields.Integer(string="Resultado Visitante", default=0)
    fecha = fields.Date(string="Fecha", default=datetime.today())


    @api.onchange('resultadoLocal', 'resultadoVisitante')
    def _onchange_resultados(self):
        pass
    
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

    
    def _jugarPartido(self):
        equipo_local, equipo_visitante = self.equipos[:2]
        if equipo_local.promedioVictorias > equipo_visitante.promedioVictorias:
            self._mejor_equipo(1, 1)
        else:
            self._mejor_equipo(1, 0)

    def _mejor_equipo(self, local, visitante):
        equipo_local, equipo_visitante = self.equipos[:2]

        if equipo_local.entrenador_id.calificacion_promedio > equipo_visitante.entrenador_id.calificacion_promedio:
            self._calcular_resultado(97 - local, 3 - visitante - 1)
        else:
            self._calcular_resultado(97 + local + 1, 3 + visitante + 1)

    def _calcular_resultado(self, porcentajeLocal, porcentajeVisitante):
        local = 0
        visitante = 0
        for _ in range(90):
            randomVar = random.randint(1, 100)
            if randomVar > porcentajeLocal:
                local += 1
            elif randomVar < porcentajeVisitante:
                visitante += 1
        
        # Actualizamos los valores usando write() para refrescar la vista
        self.write({
            'resultadoLocal': local,
            'resultadoVisitante': visitante
        })

        if local > visitante:
            self.equipos[0].write({'partidosGanados': self.equipos[0].partidosGanados + 1})
            self.equipos[1].write({'partidosPerdidos': self.equipos[1].partidosPerdidos + 1})
            self.equipos[0].entrenador_id.write({'partidos_ganados': self.equipos[0].entrenador_id.partidos_ganados + 1})
            self.equipos[1].entrenador_id.write({'partidos_perdidos': self.equipos[1].entrenador_id.partidos_perdidos + 1})
        elif local < visitante:
            self.equipos[1].write({'partidosGanados': self.equipos[1].partidosGanados + 1})
            self.equipos[0].write({'partidosPerdidos': self.equipos[0].partidosPerdidos + 1})
            self.equipos[1].entrenador_id.write({'partidos_ganados': self.equipos[1].entrenador_id.partidos_ganados + 1})
            self.equipos[0].entrenador_id.write({'partidos_perdidos': self.equipos[0].entrenador_id.partidos_perdidos + 1})

    def generar_resultado(self):

        self._jugarPartido()
        return True