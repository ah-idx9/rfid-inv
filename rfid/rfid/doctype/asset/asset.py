import frappe

def before_save(doc,method=None):
    item_barcode = frappe.db.get_value('Item',doc.item_code,'custom_barcode')
    if item_barcode:
        doc.custom_barcode = item_barcode
        