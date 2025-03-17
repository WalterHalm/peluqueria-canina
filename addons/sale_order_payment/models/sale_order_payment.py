from odoo import models, fields, api

class SaleOrderPayment(models.Model):
    _name = 'sale.order.payment'
    _description = 'Sale Order Payment'
    _order = 'payment_date desc'

    sale_order_id = fields.Many2one('sale.order', string='Orden de venta', required=True)
    partner_id = fields.Many2one(
        'res.partner', 
        string='Cliente',
        related='sale_order_id.partner_id', 
        store=True,
        readonly=True
    )
    amount = fields.Float(string='Monto a ingresar', required=True)
    payment_date = fields.Date(string='Fecha de pago', required=True, default=fields.Date.today)
    payment_method = fields.Selection([
        ('efectivo', 'Efectivo'),
        ('transferencia bancaria', 'Transferencia Bancaria'),
        ('mercado pago', 'Mercado Pago'),
        ('otro', 'Otro')
    ], string='Metodo de pago', required=True, default='efectivo')
    notes = fields.Text(string='Notas')

    @api.onchange('sale_order_id')
    def _onchange_sale_order(self):
        if self.sale_order_id:
            self.partner_id = self.sale_order_id.partner_id

