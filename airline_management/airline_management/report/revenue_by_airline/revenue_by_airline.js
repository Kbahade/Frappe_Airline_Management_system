// Copyright (c) 2025, komal and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue By Airline"] = {
	"filters": [
		{
            fieldname: 'from_date',
            label: __('From Date'),
            fieldtype: 'Date'
        },
        {
            fieldname: 'to_date',
            label: __('To Date'),
            fieldtype: 'Date'
		},
		{
			fieldname: 'airline',
			label: __('Airline'),
			fieldtype: 'Link',
			options: 'Airline'	
		}
	]
};
