
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError, ValidationError


# class estateproperty(http.Controller):
class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id
        employee_ids = request.env['hr.employee'].search(
            [('user_id', '=', request.env.user.id)]).ids
        payslip = request.env['hr.payslip'].search(
            [('employee_id', 'in', employee_ids)])
        # payslip = request.env['hr.payslip']
        if 'payslip_count' in counters:
            values['payslip_count'] = payslip.search_count([('employee_id', 'in', employee_ids)]) \
                if payslip.check_access_rights('read', raise_exception=False) else 0
        return values

#   report value get
    def _payslip_get_page_view_values(self, payslip1, access_token, **kwargs):
        values = {
            'page_name': 'payslip',
            'payslip': payslip1,
            'o': payslip1

        }
        return self._get_page_view_values(payslip1, access_token, values, 'my_payslip_history', False, **kwargs)

    @http.route('/my/payslip', type="http", auth="user", website=True)
    def hello_template(self, **kw):
        values = self._prepare_portal_layout_values()
        # partner = request.env.user.partner_id
        employee_ids = request.env['hr.employee'].search(
            [('user_id', '=', request.env.user.id)])
        print("*******************************", employee_ids)
        for e in employee_ids:
            print("\n\n\n the em name is", e.name)
        payslip = request.env['hr.payslip'].search(
            [('employee_id', 'in', employee_ids.ids)])

        print("*******************************", payslip)

        values.update({

            'payslip': payslip.sudo(),
            'page_name': 'slip',
            'default_url': '/my/payslip',


        })
        return request.render('website_payslip.portal_my_payslips', values)


     # report

    @http.route(['/my/payslip/<int:id>'], type='http', auth="public", website=True)
    def portal_order_page(self, id, report_type=None, access_token=None, message=False, download=False, **kw):
        print("***************************",access_token)

        try:
            payslip_order = self._document_check_access(
                'hr.payslip', id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=payslip_order, report_type=report_type, report_ref='hr_payroll.action_report_payslip', download=download)

        values = self._payslip_get_page_view_values(
            payslip_order, access_token, **kw)
        print("******values***********", values)
        # return request.render("hr_payroll.report_payslip", values)

        return request.render("website_payslip.payslip_portal_template", values)

