from odoo import models,api

from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = 'res.partner'

   
    @api.model
    def search_read(self, domain, fields=None, offset=0, limit=None, order=None):
        customer = self.env['ir.config_parameter'].sudo().get_param('sale_order_setting.default_customer_id')
        domain += [('id','!=',customer)]
        return super().search_read(domain=domain,fields=fields, offset=offset, limit=limit, order=order)
        
    @api.model
    def _name_search(self, name,args=None, operator='ilike', limit=100, name_get_uid=None):
      customer = self.env['ir.config_parameter'].sudo().get_param('sale_order_setting.default_costmer_id')
      args = args or []
      domain = [('id', '!=', customer)]
      return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)


