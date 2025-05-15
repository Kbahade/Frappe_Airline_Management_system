// Copyright (c) 2025, komal and contributors
// For license information, please see license.txt

frappe.ui.form.on("Flight Passenger", {
	refresh(frm) {
        if (frm.is_dirty()){
            frappe.show_alert('Please save the form before doing any changes')
        }
frappe.ui.form.on("Flight Passenger"),{
    refresh: function(frm) {
        if (frm.doc.date_of_birth) {
            var birthyear = new Date(frm.doc.date_of_birth);
            var today = new Date();
            var a = today.getFullYear() - birthyear.getFullYear()
                    // if (a < 0 || a == 0 && today.getDate() < birthyear.getDate()){
                    //     age--
                    // }
                    frm.set_value("age", a);
                    frm.refresh();
                }
            // frm.set_value("age", a);
            // frm.refresh_field("age");
            }
        }

	},
});
