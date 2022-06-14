# -*- coding: utf-8 -*-
# from odoo import http


# class ManufacturingDate(http.Controller):
#     @http.route('/manufacturing_date/manufacturing_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufacturing_date/manufacturing_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufacturing_date.listing', {
#             'root': '/manufacturing_date/manufacturing_date',
#             'objects': http.request.env['manufacturing_date.manufacturing_date'].search([]),
#         })

#     @http.route('/manufacturing_date/manufacturing_date/objects/<model("manufacturing_date.manufacturing_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufacturing_date.object', {
#             'object': obj
#         })
