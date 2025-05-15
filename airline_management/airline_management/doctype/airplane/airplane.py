# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
    
	def get_value(name, model,airline, capacity):
		doct = frappe.db.exixts("Airplane", {"model": model, "airline": airline})

		if doct:
			frappe.throw(f"Already Exist")

	

	# def validate(self):
