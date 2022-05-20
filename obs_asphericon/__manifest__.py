# -*- coding: utf-8 -*-
{
    'name': "OBS Asphericon",

    'summary': """
       Module for OBS Asphericon""",

    'description': """
        Module for OBS Asphericon which adds additional fields in Sales, CRM, Purchase modules
    """,
    'author': "Odoo Business Solutions",
    'website': "https://www.odoo.com",
    'category': 'crm',
    'version': '0.1',
    'depends': ['project_forecast', 'sale_crm', 'sale_stock', 'purchase', 'sale_timesheet',
                'account_check_printing', 'mrp', 'quality_control',
                'sale_timesheet_purchase', 'delivery', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/stock_picking_views.xml',
        'wizard/project_template_wizard.xml',
        'wizard/stock_picking_return_views.xml',
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
        'views/vendor_rating_views.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
        'views/project_opportunity_views.xml',
        'views/sale_order_views.xml',
        'views/product_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_bom_views.xml',
        'views/quality_alert_views.xml',
        'views/product_tags_views.xml',
        'views/shipping_info_views.xml',
        'views/purchase_order_line_views.xml',
        'views/sale_order_template_views.xml',
        'views/account_move_views.xml',
        'views/res_confing_settings_views.xml',
        'views/product_category_views.xml',
        'views/account_invoice_report_views.xml',
        'views/sale_report_views.xml',
        'views/stock_location_views.xml',
        'views/stock_quant_views.xml',
    ],
    'qweb': [
        'static/src/xml/project_template_button.xml',
    ],
}
