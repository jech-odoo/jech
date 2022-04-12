from odoo import models, api

from odoo.osv import expression


class ResPartner(models.Model):
    _inherit = 'res.partner'


    def name_get(self):
        result = []
        for rec in self: 
          result.append((rec.id,'%s - %s' % (rec.name,rec.zip)))
        return result
