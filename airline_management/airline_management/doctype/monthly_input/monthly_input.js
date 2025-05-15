// Copyright (c) 2025, komal and contributors
// For license information, please see license.txt

frappe.ui.form.on("Monthly Input", {
	refresh(frm) {
        frm.disable_save();
	},


    click: function(frm) {
        frappe.call({
            method:"airline_management.airline_management.doctype.monthly_input.monthly_input.get_value",
            args: {
                name1 :frm.doc.name1,
                amount: frm.doc.amount,
                fiscal_year: frm.doc.fiscal_year,
                month: frm.doc.month
            },
            callback: function(r) {
                if (!r.exc) {
                    frappe.msgprint("Record has been submitted!")
                }
            }
            
        });
    }

});
