from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_ids = fields.One2many(
        'sale.order.payment',
        'sale_order_id',
        string='Pagos'
    )
    payment_amount = fields.Float(string='Registrar nuevo pago', tracking=True)
    remaining_balance = fields.Float(string='Deuda', compute='_compute_remaining_balance', store=True)
    total_paid = fields.Float(string='Suma de los pagos', compute='_compute_total_paid', store=True)

    @api.depends('payment_ids.amount', 'amount_total')
    def _compute_remaining_balance(self):
        for order in self:
            order.remaining_balance = order.amount_total - order.total_paid

    @api.depends('payment_ids.amount')
    def _compute_total_paid(self):
        for order in self:
            order.total_paid = sum(order.payment_ids.mapped('amount'))

    def action_register_payment(self):
        if self.payment_amount <= 0:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': 'Payment amount must be greater than zero',
                    'type': 'warning',
                }
            }
        
        self.env['sale.order.payment'].create({
            'sale_order_id': self.id,
            'amount': self.payment_amount,
            'payment_date': fields.Date.today(),
        })
        self.payment_amount = 0.0  # Reset payment amount field
        return True

