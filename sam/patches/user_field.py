import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():

    df = dict(fieldname="section_break434", fieldtype="Section Break", label="GL User", insert_after="user_image")
    df1 = dict(fieldname="gl_user", fieldtype="Data", label="GL User", insert_after="section_break434")
    df3 = dict(fieldname="column_break2333", fieldtype="Column Break", insert_after="gl_user")
    df4 = dict(fieldname="gl_password", fieldtype="Password", label="GL Password",  insert_after="column_break2333")
    create_custom_field("User", df)
    create_custom_field("User", df1)
    create_custom_field("User", df3)
    create_custom_field("User", df4)
    
    frappe.db.commit()