# Copyright (c) 2025, komal and contributors
# For license information, please see license.txt


import frappe
from frappe.utils import today, getdate, add_days

def get_columns():
    return [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 200
        }
    ]



def execute(filters=None):
    
    columns = get_columns()
    data = get_data(filters)
    total_revenue = sum(d[1] or 0 for d in data)
    data_list = [list(row) for row in data]
    total_row = ["Total", total_revenue]
    chart = get_chart(data_list, total_revenue)
    
    report_summary = [{
        "value": total_revenue,
        "indicator": "Green" if total_revenue > 0 else "Red",
        "label": "Total Revenue",
        "datatype": "Currency",
        "currency": ""
    }]
    
    return columns, data_list, total_revenue, chart, report_summary

def get_data(filters):
    airline_filter = filters.get("airline") if filters else None
    
    from_date  = getdate(filters.get("from_date") or add_days(today(), -30))
    to_date = getdate(filters.get("to_date" or today()))
    if from_date > to_date:
        frappe.throw(" From Date must be before To Date")
    
    if airline_filter:
        data = frappe.db.sql("""
            SELECT
                al.name AS airline,
                SUM(at.total_amount) AS revenue
            FROM
                `tabAirline` AS al
            LEFT JOIN
                `tabAirplane` AS ai ON ai.airline = al.name
            LEFT JOIN
                `tabAirplane Flight` AS af ON af.airplane = ai.name
            LEFT JOIN
                `tabAirplane Ticket` AS at ON at.flight = af.name
            WHERE
                al.name = %s AND
                at.creation BETWEEN %s AND %s
            GROUP BY
                al.name
            ORDER BY
                revenue DESC
        """, (airline_filter, from_date, to_date))       #used it to pass a tuple value in %s to filter out airline 
    else:
        data = frappe.db.sql("""
            SELECT
                al.name AS airline,
                SUM(at.total_amount) AS revenue
            FROM
                `tabAirline` AS al
            LEFT JOIN
                `tabAirplane` AS ai ON ai.airline = al.name
            LEFT JOIN
                `tabAirplane Flight` AS af ON af.airplane = ai.name
            LEFT JOIN
                `tabAirplane Ticket` AS at ON at.flight = af.name
            WHERE
                at.creation BETWEEN %s AND %s
            GROUP BY
                al.name
            ORDER BY
                revenue DESC
        """, (from_date, to_date))
    
    return data
	

	
def get_chart(data, total_revenue):
    chart = {
        "data": {
            "labels": [d[0] for d in data[:-1]],
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d[1] for d in data[:-1]]
                }
            ]
        },
        "type": "donut",
        "center": {
            "text": "Total Revenue",
            "subtext": frappe.format_value(total_revenue, dict(fieldtype='Currency')),
            "style": {
                "fill": "green",
                "font-size": "14px",
                "font-weight": "bold"
            }
        }
    }

    return chart



