# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persona(models.Model):
    _name = 'futbol_master.persona'
    _description = 'Persona'

    name = fields.Char(string="Nombre")
    edad = fields.Integer(string="Edad", required=True)
    genero = fields.Selection([ ("1","Masculino"), ("2","Femenino")],string="Genero")
    pais = fields.Selection([
        ('AF', 'Afganistán'), ('AL', 'Albania'), ('DZ', 'Argelia'), ('AS', 'Samoa Americana'), ('AD', 'Andorra'),
        ('AO', 'Angola'), ('AI', 'Anguila'), ('AQ', 'Antártida'), ('AG', 'Antigua y Barbuda'), ('AR', 'Argentina'),
        ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaiyán'),
        ('BS', 'Bahamas'), ('BH', 'Baréin'), ('BD', 'Bangladés'), ('BB', 'Barbados'), ('BY', 'Bielorrusia'),
        ('BE', 'Bélgica'), ('BZ', 'Belice'), ('BJ', 'Benín'), ('BM', 'Bermudas'), ('BT', 'Bután'),
        ('BO', 'Bolivia'), ('BA', 'Bosnia y Herzegovina'), ('BW', 'Botsuana'), ('BR', 'Brasil'), ('BN', 'Brunéi'),
        ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Camboya'),
        ('CM', 'Camerún'), ('CA', 'Canadá'), ('KY', 'Islas Caimán'), ('CF', 'República Centroafricana'), ('TD', 'Chad'),
        ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'), ('KM', 'Comoras'), ('CG', 'Congo'),
        ('CD', 'República Democrática del Congo'), ('CR', 'Costa Rica'), ('CI', 'Costa de Marfil'), ('HR', 'Croacia'), ('CU', 'Cuba'),
        ('CY', 'Chipre'), ('CZ', 'Chequia'), ('DK', 'Dinamarca'), ('DJ', 'Yibuti'), ('DM', 'Dominica'),
        ('DO', 'República Dominicana'), ('EC', 'Ecuador'), ('EG', 'Egipto'), ('SV', 'El Salvador'), ('GQ', 'Guinea Ecuatorial'),
        ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Esuatini'), ('ET', 'Etiopía'), ('FJ', 'Fiyi'),
        ('FI', 'Finlandia'), ('FR', 'Francia'), ('GA', 'Gabón'), ('GM', 'Gambia'), ('GE', 'Georgia'),
        ('DE', 'Alemania'), ('GH', 'Ghana'), ('GR', 'Grecia'), ('GD', 'Granada'), ('GU', 'Guam'),
        ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bisáu'), ('GY', 'Guyana'), ('HT', 'Haití'),
        ('HN', 'Honduras'), ('HU', 'Hungría'), ('IS', 'Islandia'), ('IN', 'India'), ('ID', 'Indonesia'),
        ('IR', 'Irán'), ('IQ', 'Irak'), ('IE', 'Irlanda'), ('IL', 'Israel'), ('IT', 'Italia'),
        ('JM', 'Jamaica'), ('JP', 'Japón'), ('JO', 'Jordania'), ('KZ', 'Kazajistán'), ('KE', 'Kenia'),
        ('KI', 'Kiribati'), ('KR', 'Corea del Sur'), ('KW', 'Kuwait'), ('KG', 'Kirguistán'),
        ('LA', 'Laos'), ('LV', 'Letonia'), ('LB', 'Líbano'), ('LS', 'Lesoto'), ('LR', 'Liberia'),
        ('LY', 'Libia'), ('LI', 'Liechtenstein'), ('LT', 'Lituania'), ('LU', 'Luxemburgo'), ('MG', 'Madagascar'),
        ('MW', 'Malaui'), ('MY', 'Malasia'), ('MV', 'Maldivas'), ('ML', 'Malí'), ('MT', 'Malta'),
        ('MH', 'Islas Marshall'), ('MR', 'Mauritania'), ('MU', 'Mauricio'), ('MX', 'México'), ('FM', 'Micronesia'),
        ('MD', 'Moldavia'), ('MC', 'Mónaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MA', 'Marruecos'),
        ('MZ', 'Mozambique'), ('MM', 'Birmania'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'),
        ('NL', 'Países Bajos'), ('NZ', 'Nueva Zelanda'), ('NI', 'Nicaragua'), ('NE', 'Níger'), ('NG', 'Nigeria'),
        ('MK', 'Macedonia del Norte'), ('NO', 'Noruega'), ('OM', 'Omán'), ('PK', 'Pakistán'), ('PW', 'Palaos'),
        ('PS', 'Palestina'), ('PA', 'Panamá'), ('PG', 'Papúa Nueva Guinea'), ('PY', 'Paraguay'), ('PE', 'Perú'),
        ('PH', 'Filipinas'), ('PL', 'Polonia'), ('PT', 'Portugal'), ('QA', 'Catar'), ('RO', 'Rumanía'),
        ('RU', 'Rusia'), ('RW', 'Ruanda'), ('KN', 'San Cristóbal y Nieves'), ('LC', 'Santa Lucía'), ('VC', 'San Vicente y las Granadinas'),
        ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Santo Tomé y Príncipe'), ('SA', 'Arabia Saudita'), ('SN', 'Senegal'),
        ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leona'), ('SG', 'Singapur'), ('SK', 'Eslovaquia'),
        ('SI', 'Eslovenia'), ('SB', 'Islas Salomón'), ('SO', 'Somalia'), ('ZA', 'Sudáfrica'), ('SS', 'Sudán del Sur'),
        ('ES', 'España'), ('LK', 'Sri Lanka'), ('SD', 'Sudán'), ('SR', 'Surinam'), ('SE', 'Suecia'),
        ('CH', 'Suiza'), ('SY', 'Siria'), ('TW', 'Taiwán'), ('TJ', 'Tayikistán'), ('TZ', 'Tanzania'),
        ('TH', 'Tailandia'), ('TL', 'Timor Oriental'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad y Tobago'),
        ('TN', 'Túnez'), ('TR', 'Turquía'), ('TM', 'Turkmenistán'), ('TV', 'Tuvalu'), ('UG', 'Uganda'),
        ('UA', 'Ucrania'), ('AE', 'Emiratos Árabes Unidos'), ('GB', 'Reino Unido'), ('US', 'Estados Unidos'), ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistán'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'),
        ('ZM', 'Zambia'), ('ZW', 'Zimbabue')
    ], string="País")

    @api.onchange('edad')
    def comprobar_edad(self):
        if self.edad < 16:
            self.edad = 16
        elif self.edad > 100:
            self.edad = 100