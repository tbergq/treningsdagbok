
function loadRegisterPartial(element) {
	
	var exercise_id = $(element).attr('id');
	var name = $(element).attr('data-name');
	$("tr").removeClass("selected-exercise");
	$(element).parent().parent().addClass("selected-exercise");
	$.ajax({
		url : "/workout/register_partial/" + day_id + "/" + exercise_id + "/",
		type : "GET"	
	}).done(function(data){
		
		$(".modal-body").html(data);
		$(".modal-header").html(name);
		$("#myModal").modal('show');
	}).error(function(data){
		
	});
	
	
}





$(document).ready(function() {
	if(started) {
		
	} else {
		var buttons = $(".register-button");
		
		for(var i = 0; i < buttons.length; i++) {
			buttons[i].disabled = true;
		}
	}
});