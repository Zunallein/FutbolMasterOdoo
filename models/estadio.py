from odoo import models, fields, api


class Estadio(models.Model):
    _name = 'futbol_master.estadio'
    _description = 'futbol_master.estadio'

    name = fields.Char()
    pais = fields.Many2one('res.country', string="País",required=True)
    provincia = fields.Many2one('res.country.state', string="Provincia",required=True, 
                    domain=([('res.country.state.country_id', '=', '0')]), 
                    attrs="{'readonly': [('pais', '=', False)]}")
    capacidad = fields.Integer(string="Capacidad", required=True)

    @api.onchange('pais')
    def _cambio_provincia(self):
        self.provincia = False
        return {
            'domain': {
                'provincia': [('country_id', '=', self.pais.id)]
            }
        }