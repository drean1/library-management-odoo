{
    "name": "Library Management",
    "version": "1.0",
    "summary": "Library Book Management",
    "category": "Services",
    "author": "Andrean",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/member_views.xml",
        "views/loan_views.xml",
        "views/menus.xml",
    ],
    "application": True,
    "installable": True,
}
