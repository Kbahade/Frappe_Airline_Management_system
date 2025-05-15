# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airline(Document):
	frappe.db.add_unique("Airline",["customer_care_number"])
