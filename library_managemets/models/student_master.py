from odoo import fields, models

class student_master(models.Model):
    _name = "student.master"
    _description = "Library Management"

    student = fields.Char(default="Unknown")
    r_no = fields.Integer()
    city = fields.Char()
    image = fields.Image()
    date_availability = fields.Date(copy=False)
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    description=fields.Char()
    book_id=fields.Many2one('book.master')
    book_line_ids=fields.One2many('book.master','student_id')
   

