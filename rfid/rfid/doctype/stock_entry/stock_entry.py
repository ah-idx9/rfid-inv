import frappe
import itertools

def on_submit(doc,method=None):
    item_code,name = frappe.db.get_value('Serial No',{'purchase_document_no':doc.name},['item_code','name'])
    serial_item_code = item_code+name
    ascii_list = list(itertools.chain(*map(lambda x: map(ord, x), serial_item_code)))
    ascii_list_new = (''.join(map(str, ascii_list)))

    frappe.db.set_value('Serial No',{'purchase_document_no':doc.name},'custom_barcode',ascii_list_new)
    frappe.db.commit()