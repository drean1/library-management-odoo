# Library Management System — Odoo 19

A simple Library Management System module built with Odoo 19 to manage books, library members, and book loans.

## Features

- **Book Management** — Manage book names, authors, ISBNs, and stock quantities.
- **Stock Availability** — Automatically determine whether a book is available based on its stock.
- **Member Management** — Store member information, including names, email addresses, and phone numbers.
- **Loan Management** — Record book loans, members, loan dates, due dates, and return dates.
- **Data Validation** — Validate book stock and loan dates.
- **Access Control** — Configure model access permissions.

## Tech Stack

- Odoo 19
- Python
- PostgreSQL
- XML
- Odoo ORM
- Docker & Docker Compose
- Git & GitHub

## Project Structure

```text
library-management-odoo/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── members.py
│   └── loan.py
├── security/
│   └── ir.model.access.csv
└── views/
    ├── book_views.xml
    ├── member_views.xml
    ├── loan_views.xml
    └── menus.xml
```

## Data Models

- `library_book` — Stores book information and stock availability.
- `library_member` — Stores library member information.
- `library_loan` — Records book loans and their status.

## Setup

This module is designed to run on Odoo 19 with PostgreSQL. Docker Compose can be used to run the development environment.

1. Clone this repository:

   ```bash
   git clone https://github.com/drean1/library-management-odoo.git
   ```

2. Place the module in an Odoo add-ons directory.
3. Configure the Odoo add-ons path to include the module's parent directory.
4. Start Odoo and PostgreSQL.
5. Open the Odoo web interface.
6. Enable Developer Mode and update the Apps list.
7. Install **Library Management** from the Apps menu.

## Development Status

The core book, member, and loan models and their views have been implemented. Further testing and improvements are ongoing, including the book-return workflow and validation checks.

## Author

**Andrean**

GitHub: [@drean1](https://github.com/drean1)
