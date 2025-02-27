# Copyright (c) 2025, vstdeveloper and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils import getdate
from frappe import _


class Task(Document):
	def validate(self):
		project = frappe.get_doc("Project", self.project)
		if getdate(self.task_dd) > getdate(project.proj_ex_sd):
			frappe.throw(_("Task End Date must be on or before the Project's End Date"))
		if getdate(self.task_dd) > getdate(project.proj_ex_ed):
			frappe.throw(_("Task End Date must be on or before the Project's End Date"))
	pass
