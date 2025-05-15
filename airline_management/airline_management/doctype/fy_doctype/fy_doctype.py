# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FYDoctype(Document):
	def validate(self):
		self.check_duplicate()

	def check_duplicate(self):
		duplicate = frappe.db.exists(
			"FY Doctype",
			{
				"fy_name": self.fy_name,
				# "fy_starting_date": self.fy_starting_date,
				# "fy_ending_date": self.fy_ending_date
			}
		)

		if duplicate and duplicate != self.name:
			frappe.throw("A fiscal year with same name already exists")





