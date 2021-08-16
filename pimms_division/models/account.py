from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    division_id = fields.Many2one(
        'pimms.division', ondelete='restrict', string='Division'
    )

    def _get_name_invoice_report(self):
        self.ensure_one()

        if self.division_id:
            return self.division_id.invoice_layout_id.get_xml_id()[self.division_id.invoice_layout_id.id]
        return super(AccountMove, self)._get_name_invoice_report()
