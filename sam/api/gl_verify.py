import frappe
from frappe import _
from frappe.utils.password import get_decrypted_password

@frappe.whitelist()
def get_user(user=None):
    user = user
    # frappe.throw(f"{frappe.session.user} is not allowed to access this API",)
    if not frappe.has_permission("User", "read"):
        frappe.throw(_("You do not have permission to access this resource."))
    if not frappe.db.exists("User", user):
        frappe.throw(_("User not Found in user Doc"))
    
    doc = frappe.get_doc("User", user)
    gl_password = get_decrypted_password("User", doc.name, "gl_password", raise_exception=False)

    return {
        "email": doc.email,
        "gl_password": gl_password,
    }