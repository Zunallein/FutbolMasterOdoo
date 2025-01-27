# -*- coding: utf-8 -*-
# from odoo import http


# class FutbolMaster(http.Controller):
#     @http.route('/futbol_master/futbol_master', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/futbol_master/futbol_master/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('futbol_master.listing', {
#             'root': '/futbol_master/futbol_master',
#             'objects': http.request.env['futbol_master.futbol_master'].search([]),
#         })

#     @http.route('/futbol_master/futbol_master/objects/<model("futbol_master.futbol_master"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('futbol_master.object', {
#             'object': obj
#         })
