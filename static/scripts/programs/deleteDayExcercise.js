
function loadDeleteExcerciseWarning(element) {
	
	$.ajax({
		url : $(element).attr('data-url'),
		type : "GET",
	}).done(function(data) {
		$(".modal-body").html(data);
		$(".modal-footer").html('<button type="button" class="btn btn-default" data-dismiss="modal">Lukk</button>');
		$("#myModal").modal('show');
	});
}