
function showDayClick(element) {
	var url = element.getAttribute('data-url');
	loadDayForModal(url);
}

function clickLoadWarning(element) {
	var url = element.getAttribute('data-url');
	loadDeleteWarning(url);
}

function loadDayForModal(url) {
	$.ajax({
		url : url,
		type : "GET"
	}).done(function(data){
		$(".modal-body").html(data);
		var linkToDay = '<button type="button" class="btn btn-default" data-dismiss="modal">Lukk</button>' +  
			'<a href="/programs/add_exercise_to_day/' + dayProgramId + '/" class="btn btn-primary">Gå til dag</a>';
		$(".modal-footer").html(linkToDay);
		$('#myModal').modal('show');		
	});
}

function resetFooter() {
	$(".modal-footer").html('<button type="button" class="btn btn-default" data-dismiss="modal">Lukk</button>');
	$('#myModal').modal('hide');
}

function loadDeleteWarning(url) {
	$.ajax({
		url : url,
		type :"GET"
	}).done(function(data) {
		$(".modal-body").html(data);
		$('#myModal').modal('show');
	});
}