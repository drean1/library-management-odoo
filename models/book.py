from odoo import fields, models

class LibraryBook(models.Model):
    _name = "library_book"
    _description = "Library Model"

    name = fields.Char(required=True)
    author = fields.Char(string= 'Author')
    isbn = fields.Char(string= 'Isbn')
    stock = fields.Integer(string='Stock', default=0)
    available = fields.Boolean(string= 'Available')