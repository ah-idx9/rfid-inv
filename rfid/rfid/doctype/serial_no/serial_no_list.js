frappe.listview_settings['Serial No'] = {
    onload: function(me) {
		me.page.add_action_item('Print RFID', function() {
			frappe.msgprint('RFID Printed')
            // const boq = me.get_checked_items();
            // frappe.call({
            //       method: "reneworld.api.boq_name",
            //       freeze: true,
            //       args:{
            //             "items": boq
            //       },
            //       callback: function (r) {
            //             if (r.message) {
            //                   frappe.set_route("query-report", "BOQ Stock Report",
            //                   { boq: r.message});
            //             }
            //       }
            // });
		});
	},
}