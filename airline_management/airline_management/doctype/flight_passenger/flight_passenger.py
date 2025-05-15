# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class FlightPassenger(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'

	def validate(self):
		if self.date_of_birth > today():
			frappe.throw("Please select valid birth date")

