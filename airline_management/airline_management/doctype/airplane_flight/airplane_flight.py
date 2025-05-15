# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import add_to_date, now_datetime

class AirplaneFlight(Document):
    def on_save(self):
        
        self.status = "Completed"
        self.save()

    
def validate(self):
    if self.time_of_departure and self.duration:
        expected_arrival = add_to_date(
            self.time_of_departure,
            hours=self.duration
        )
        if expected_arrival <= now_datetime():
            self.status = "Completed"

class AirplaneFlight(WebsiteGenerator):
    def get_page_info(self):
        return {
            "published": self.is_published,
        }
    def on_submit(self):
        
        self.status = "Completed"
        if self.status != "Completed":
            frappe.thorw("Change the status of the docoument to submit the document.")
        # frappe.throw("Change the status to Completed to Submit.")
        self.save()




