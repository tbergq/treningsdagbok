$(document).ready(function() {

	$(".add-member").click(function() {
		$.ajax({
			url : '/group/invite/',
			type : "GET",
			data : {
				group_id : $(this).attr('data-id')
			},
		}).done(function(data) {
			$(".modal-body").html(data);
			$(".modal-footer").html('');
			$("#myModal").modal('show');
		});
	});

	$(".add-program").click(function() {
		$.ajax({
			url : '/group/show_programs_to_add/',
			type : "GET",
			data : {
				group_id : $(this).attr('data-id')
			},
		}).done(function(data) {
			$(".modal-body").html(data);
			$(".modal-footer").html('');
			$("#myModal").modal('show');
		});
	});
});

/*function confirmAdd(button) {
	$.ajax({
		url : '/group/add_program/' + $(button).attr('data-program-id') + '/' +  groupId + '/',
		type : 'POST',
		
	}).done(function(data){
		document.open();
		document.write(data);
		document.close();
	});
}*/




