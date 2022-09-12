# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

import frappe


def execute():
	frappe.reload_doc("core", "doctype", "system_settings", force=1)
	frappe.db.set_value("System Settings", None, "password_reset_limit", 3)
