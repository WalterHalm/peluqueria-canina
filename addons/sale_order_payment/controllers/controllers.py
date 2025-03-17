# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderPayment(http.Controller):
#     @http.route('/sale_order_payment/sale_order_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_payment/sale_order_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_payment.listing', {
#             'root': '/sale_order_payment/sale_order_payment',
#             'objects': http.request.env['sale_order_payment.sale_order_payment'].search([]),
#         })

#     @http.route('/sale_order_payment/sale_order_payment/objects/<model("sale_order_payment.sale_order_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_payment.object', {
#             'object': obj
#         })

