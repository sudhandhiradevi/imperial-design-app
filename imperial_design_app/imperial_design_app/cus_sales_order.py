def calculate_total_weight(doc,methods):
    from frappe.utils import flt
    total_wt = 0.0

    for d in doc.items:
        d.weight = flt(d.weight_per_unit) * flt(d.qty)
        total_wt += d.weight

    doc.total_wt = total_wt    