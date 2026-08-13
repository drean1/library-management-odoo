from odoo import fields, models

class LibraryMember(models.Model):
    _name = "library_member"
    _description = "Library Member"

    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    member_code = fields.Char(string="Member Code")
    active = fields.Boolean(default=True)