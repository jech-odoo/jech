from odoo import fields, models

class book_master(models.Model):
    _name = "book.master"
    

    # book_ids = fields.One2many('student.master','book_id')
    price = fields.Integer()
    author_id=fields.Many2one('author.master')
    publisher = fields.Char(string='publisher name')
    # book_id = fields.Many2one('author.master')
    name=fields.Char(string='Book Name')
    book_id=fields.Many2one('book.master')
    # book_id=fields.Many2one('book.master')
    student_id = fields.Many2one('student.master')
  