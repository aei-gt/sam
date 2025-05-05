import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    frappe.delete_doc("Custom Field","User-gl_password")
    frappe.delete_doc("Custom Field","User-column_break2333")
    frappe.delete_doc("Custom Field","User-gl_user")
    frappe.delete_doc("Custom Field","User-section_break434")
    frappe.db.commit()