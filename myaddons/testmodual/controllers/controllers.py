# -*- coding: utf-8 -*-
from odoo import http

# class Testmodual(http.Controller):
#     @http.route('/testmodual/testmodual/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testmodual/testmodual/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testmodual.listing', {
#             'root': '/testmodual/testmodual',
#             'objects': http.request.env['testmodual.testmodual'].search([]),
#         })

#     @http.route('/testmodual/testmodual/objects/<model("testmodual.testmodual"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testmodual.object', {
#             'object': obj
#         })