from odoo import api, fields, models, _ 


class Division(models.Model):
    _name = 'pimms.division'
    _description = 'Division'

    name = fields.Char(required=True, string='Division Name')

    company_id = fields.Many2one(
        'res.company', 
        default=lambda self: self.env.company, ondelete='cascade',
        string='Company')

    logo = fields.Binary(string='Division Logo')
    invoice_layout_id = fields.Many2one(
        'ir.ui.view', ondelete='restrict', required=True,
        string='Invoice Layout'
    )
    statement_layout_id = fields.Many2one(
        'ir.ui.view', ondelete='restrict', required=True,
        string='Statement Layout'
    )

    _sql_constraint = [
        ('uniq_company_name', 'company_id', 'name',
            'Division name must be unique'),
    ]
