from odoo import api, fields, models
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = "library_book"
    _description = "Library Model"

    name = fields.Char(required=True)
    author = fields.Char(string= 'Author')
    isbn = fields.Char(string= 'Isbn')
    stock = fields.Integer(string='Stock', default=0)
    available = fields.Boolean(
        string="Available",
        compute= "_compute_available",
        store=True,
    )

    @api.depends("stock")
    def _compute_available(self):
        for book in self:
            book.available = book.stock > 0

    @api.constrains("stock")
    def _check_stock(self):
        for book in self:
            if book.stock < 0:
                raise ValidationError("Stock buku tidak boleh kurang dari 0.")
