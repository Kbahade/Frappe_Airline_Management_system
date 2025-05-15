
# Copyright (c) 2024, Komal Bahade and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate()
        
        if not self.flight_price:
            frappe.throw("Please provide a flight price.")

        total_amount = self.flight_price

        
        if self.add_ons:
            for item in self.add_ons:
                if item.amount:
                    total_amount += item.amount

        self.total_amount = total_amount

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("The ticket can only be submitted if the status is Boarded.")

    def remove_duplicate(self):
        unique_add_ons = {}
        for a in self.add_ons:
            key = a.item
            if key not in unique_add_ons:
                unique_add_ons[key] = a
            else:
                frappe.msgprint(f"The item '{key}' already exists and has been removed.")
        self.set("add_ons", list(unique_add_ons.values()))

    def before_insert(self):
        self.seat = f"{random.randint(1, 100)}{random.choice('ABCDE')}"

    # def on_submit(self):
    #     # self.db.set("status", "Boarded")
    #     self.status = "Boarded"

    
    def on_update(self):
            self.check_capacity()

    def check_capacity(self):
        if self.flight:
        
            ticket_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})
            flight = frappe.get_doc("Airplane Flight", self.flight)
            if flight:
                airplane = frappe.get_doc("Airplane", flight.airplane)
                if ticket_count > airplane.capacity:
                    frappe.throw("Number of tickets exceeds airplane capacity. Cannot create Airplane Ticket.")