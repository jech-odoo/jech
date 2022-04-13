from odoo import fields, models

class author_master(models.Model):
    _name = "author.master"
    
    name=fields.Char()
    # author_id=fields.Many2one('author.master')
    # author_name = fields.One2many('book.master','author_id',)
    author_book=fields.Many2one('book.master')
  
  