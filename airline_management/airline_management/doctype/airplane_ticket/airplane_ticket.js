// Copyright (c) 2025, komal and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	// refresh(frm) {
    //     frm.email_doc('Hello ${frm.doc.passenger}');

	// },
    onload: function(frm) {
        frm.fields_dict['flight'].get_query = function(doc) {
            return{
                filters: {
                    'date_of_departure': [">", frappe.datetime.get_today()]
                }
            };
        };
    }
});

