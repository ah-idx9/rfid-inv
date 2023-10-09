# Copyright (c) 2023, RFID and contributors
# For license information, please see license.txt

import frappe
import itertools
from frappe.model.document import Document

class RFIDPrintQueue(Document):
	pass

	def before_save(doc,method=None):
		doc.status = 'Pending'
		ascii_list = list(itertools.chain(*map(lambda x: map(ord, x), doc.item_code)))
		barcode = (''.join(map(str, ascii_list)))
		doc.rfid = barcode
