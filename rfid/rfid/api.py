import frappe
import json
import itertools

@frappe.whitelist()
def create_print_rfid(doc):
    doc = json.loads(doc)
    
    if doc.get('items'):
        for item in doc.get('items'):
            rfid_doc = frappe.new_doc('RFID Print Queue')
            rfid_doc.item_code = item.get('item_code')
            rfid_doc.qty = item.get('qty')
            rfid_doc.status = 'Pending'
            ascii_list = list(itertools.chain(*map(lambda x: map(ord, x), item.get('item_code'))))
            barcode = (''.join(map(str, ascii_list)))
            rfid_doc.rfid = barcode
            rfid_doc.flags.ignore_permissions = 1
            rfid_doc.save()
        frappe.msgprint('RFID Added In Print Queue')

@frappe.whitelist()
def create_print_rfid_manually(doc):
    doc = json.loads(doc)
    
    if doc:
        rfid_doc = frappe.new_doc('RFID Print Queue')
        rfid_doc.item_code = doc.get('item_code')
        rfid_doc.qty = doc.get('qty')
        rfid_doc.status = 'Pending'
        ascii_list = list(itertools.chain(*map(lambda x: map(ord, x), doc.get('item_code'))))
        barcode = (''.join(map(str, ascii_list)))
        rfid_doc.rfid = barcode
        rfid_doc.flags.ignore_permissions = 1
        rfid_doc.save()
    frappe.db.commit()

