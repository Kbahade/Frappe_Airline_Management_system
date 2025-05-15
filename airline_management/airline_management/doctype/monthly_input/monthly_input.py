# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyInput(Document):
    def after_insert(self):
        pass

@frappe.whitelist()
def get_value(fiscal_year, name1, amount, month):
    fiscal_doc_name = frappe.db.exists("FY Monthly Entry", {"fiscal_year": fiscal_year, "month": month})
    

    if fiscal_doc_name:
        fiscal_doc = frappe.get_doc("FY Monthly Entry", fiscal_doc_name)
        
        duplicate_found = False
        for row in fiscal_doc.child_table:
            if row.name1 == name1:
                duplicate_found = True
                break
        
        if duplicate_found:
            frappe.throw(f"Duplicate Entry: {name1} already exists for month {month} in fiscal year {fiscal_year}.")
        else:
        
            fiscal_doc.append("child_table", {
                "name1": name1,
                "amount": amount,
                "month": month,
                "fiscal_year": fiscal_year
            })
            fiscal_doc.save()
            frappe.msgprint(f"Added {name1} to {month} in fiscal year {fiscal_year}.")
    else:
        
        fiscal_doc = frappe.new_doc("FY Monthly Entry")
        fiscal_doc.fiscal_year = fiscal_year
        fiscal_doc.month = month
        fiscal_doc.append("child_table", {
            "name1": name1,
            "amount": amount,
            "month": month,
            "fiscal_year": fiscal_year
        })
        fiscal_doc.save()
        frappe.msgprint(f"New fiscal year document created for {month} {fiscal_year} and {name1} added.")

# fiscal_doc = frappe.db.exist("FY Monthly Entry", {"fiscal_year" : fiscal_year, "month" :month, })
#     if fiscal_doc:
#         frappe.get_doc("FY Monthly Entry", {"fiscal_year" : fiscal_year, "month" : month})
#     else:
#         frappe.new_doc("FY Monthly Entry", {"fiscal_year" : fiscal_year, "month" : month})

#     duplicate_found = False
#     for row in fiscal_doc.child_table:
#         if row.name1 == name1:
#             frappe.throw(f"Duplicate name found")
#         else:
#             fiscal_doc.append("child_table")
#             {
#                 "name1" = name1,
#                 "amount" = amount,
#                 "month" = month,
#                 "fiscal_year" = fiscal_year

#             }


# import frappe
# from frappe.model.document import Document

# class MonthlyInput(Document):
#     def after_insert(self):
#         pass

# @frappe.whitelist()

# def get_value(fiscal_year, name1, amount, month):
#     fiscal_doc_name = frappe.db.exists("FY Monthly Entry", {"fiscal_year": fiscal_year})

#     if fiscal_doc_name:
#         fiscal_doc = frappe.get_doc("FY Monthly Entry", fiscal_doc_name)
#     else:
#         fiscal_doc = frappe.new_doc("FY Monthly Entry")
#         fiscal_doc.fiscal_year = fiscal_year
#         fiscal_doc.month = month

    
#     duplicate_found = False
#     for row in fiscal_doc.child_table:
#         if row.name1 == name1:
#             duplicate_found = True
#             break

#     if duplicate_found:
#         frappe.throw(f"Duplicate Entry: {name1} already exists for month {month} in fiscal year {fiscal_year}.")
#     else:
    
#         fiscal_doc.append("child_table", {
#             "name1": name1,
#             "amount": amount,
#             "month": month,
#             "fiscal_year": fiscal_year
#         })

        
#         fiscal_doc.save()
#         frappe.msgprint("Record Added Successfully")


# import frappe
# from frappe.model.document import Document


# class MonthlyInput(Document):
# 	def after_insert(self):
# 		pass
	
# @frappe.whitelist()
# def get_value(fiscal_year, name1, amount, month):
# 	fiscal_doc_name = frappe.db.exists("FY Monthly Entry", {"fiscal_year": fiscal_year})
# 	# fiscal_doc.fiscal_year = fiscal_year

# 	if fiscal_doc_name:
# 		fiscal_doc = frappe.get_doc("FY Monthly Entry", fiscal_doc_name)
# 	else:
# 		fiscal_doc = frappe.new_doc("FY Monthly Entry")
# 		fiscal_doc.fiscal_year = fiscal_year
# 		fiscal_doc.month = month

# 	# if fiscal_doc.fiscal_year == fiscal_year:
# 	# 	if fiscal_doc.month == month:
# 	for row in fiscal_doc.child_table:
# 		if row.name1 == name1 and row.fiscal_year == fiscal_year and row.month == month:
# 			frappe.throw(f"Duplicate Entry: {name1} already exists for month {month} in fiscal year {fiscal_year}.")


# 	fiscal_doc.append("child_table", {
# 	 "name1": name1,
# 	 "amount": amount,
# 	 "month": month,
# 	 "fiscal_year": fiscal_year
# 	 })
		
# 	fiscal_doc.save()
# 	frappe.msgprint("Record Added Successfully")
# 		# frappe.db.commit()






