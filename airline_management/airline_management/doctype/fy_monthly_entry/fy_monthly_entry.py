# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FYMonthlyEntry(Document):
	def validate(self):
		# self.check_duplicate()
		self.update_total_amount()
	
	# def check_duplicate(self):
	# 	names = set()
	# 	# duplicates = []

	# 	for row in self.child_table:
	# 		key = (row.name1, self.fiscal_year, self.month)

	# 		if key in names:
	# 			frappe.throw(f"Duplicate Entry: {row.name1} already exists for month {self.month} in fiscal year {self.fiscal_year}.")
	# 		else:
	# 			names.add(key)
			
		# if duplicates:
		# 	duplicate_list = ", ".join(set(duplicates))
		# 	frappe.throw(f"This name is already in record: {duplicate_list}")
		
		
	def update_total_amount(self):
		total = 0
		for row in self.child_table:
			total += float(row.amount or 0)

		self.total_amount = total
    


