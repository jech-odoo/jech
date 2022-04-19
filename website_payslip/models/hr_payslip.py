
from odoo import models,_


class Payslip(models.Model):
    _name = 'hr.payslip'
    _inherit = ['portal.mixin', 'hr.payslip']

    def _get_report_base_filename(self):
        return "{} - {}".format(("Payslip"), self.number)

    def _compute_access_url(self):
        super()._compute_access_url()
        for record in self:
            record.access_url = "/my/payslip/%s" % (record.id)


    # def _compute_type_name(self):
    #     for record in self:
    #         record.type_name = _('Payslip') if record.state in ('draft', 'sent', 'cancel') else _('Pay Slip')
