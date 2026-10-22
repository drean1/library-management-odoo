from odoo import api, fields, models
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = "library_loan"
    _description = "Library Loan"
    _order = "loan_date desc"

    book_id = fields.Many2one(
        "library_book",
        string="Book",
        required=True,
    )
    member_id = fields.Many2one(
        "library_member",
        string="Member",
        required=True,
    )
    loan_date = fields.Date(
        string="Loan Date",
        required=True,
        default=fields.Date.context_today,
    )
    due_date = fields.Date(
        string="Due Date",
        required=True,
    )
    return_date = fields.Date(string="Return Date")
    state = fields.Selection(
        [
            ("borrowed", "Borrowed"),
            ("returned", "Returned"),
        ],
        string="Status",
        default="borrowed",
        required=True,
    )

    @api.constrains("loan_date", "due_date")
    def _check_dates(self):
        for loan in self:
            if loan.due_date < loan.loan_date:
                raise ValidationError(
                    "Due date tidak boleh sebelum loan date."
                )
