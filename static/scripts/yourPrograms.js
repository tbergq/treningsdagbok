


function deleteProgram(element) {
	$.ajax({
		url : $(element).attr('data-url'),
		type : "GET",
		
	}).done(function(data) {
		$(".modal-body").html(data);
		$(".modal-footer").html('');
		$("#myModal").modal('show');
	});
}