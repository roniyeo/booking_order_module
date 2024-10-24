{
    'name': "booking_order_RONIZEKI_24102024",
    'summary': """
        Booking Order Module""",
    'description': """
        Booking Order Module by Roni Zeki
    """,
    'author': "Roni Zeki",
    'website': "https://www.linkedin.com/in/roni-zeki-02a452129/",
    'category': 'Sales',
    'version': '1.0',
    'installable': True,
    'application': True,
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/canceled_order_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/work_order_view.xml',
        'views/booking_order_view.xml',
        'views/service_team_view.xml',
        'views/menu.xml',
        'report/report_work_order.xml',
        'report/report.xml',
        'data/data.xml'
    ],
}
