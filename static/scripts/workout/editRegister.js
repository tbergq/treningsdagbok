var readyExecuted = false;
$(document).ready(function() {
	if(!readyExecuted) {
		
		$(".modal-opener").each(function(){
			$(this).click(function(){
				id = $(this).attr('data-reg-id');
				name = $(this).attr('data-name')
				loadRegisterData(id, name);
			});
		});
		
		readyExecuted = true;
	}
	
	
});


function loadRegisterData(id, name) {
	$.ajax({
		url : '/workout/edit_exercise/',
		type : "GET",
		data : {id : id}
	}).done(function(data) {
		$(".modal-body").html(data);
		$("#myModal").modal('show');
		$(".modal-header").html(name);
	});
}