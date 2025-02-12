from odoo import models, fields, api


class Club(models.Model):
    _name = 'futbol_master.club'
    _description = 'futbol_master.club'

    name = fields.Char()
    equipo_id = fields.One2many("futbol_master.equipo", "club_id", string="Equipos")
    fechaCreacion = fields.Date(string="Fecha de Creacion", readonly=True)
    pais = fields.Many2one('res.country', string="País")
    provincia = fields.Many2one('res.country.state', string="Provincia",required=True, 
                    domain=([('res.country.state.country_id', '=', '0')]), 
                    attrs="{'readonly': [('pais', '=', False)]}")

    @api.constrains('fechaCreacion')
    def _value_pc(self):
        self.fechaCreacion = fields.Date.today()
        self.fechaCreacion = self.fechaCreacion.strftime("%d/%m/%Y")

    @api.onchange('pais')
    def _cambio_provincia(self):
        self.provincia = False
        return {
            'domain': {
                'provincia': [('country_id', '=', self.pais.id)]
            }
        }
