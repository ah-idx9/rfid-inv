import frappe
import itertools

def before_save(doc,method=None):
    ascii_list = list(itertools.chain(*map(lambda x: map(ord, x), doc.item_code)))
    ascii_list_new = (''.join(map(str, ascii_list)))
    doc.custom_barcode = ascii_list_new