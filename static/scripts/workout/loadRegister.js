
function loadRegisterPartial(element) {
	var exercise_id = $(element).attr('id');
	console.log(exercise_id);
	$.ajax({
		url : "/workout/register_partial/" + day_id + "/" + exercise_id + "/",
		type : "GET"	
	}).done(function(data){
		$("#registerDiv").html(data);
	}).error(function(data){
		//alert(data.status);
	});
}

$(document).ready(function() {
	if(started) {
		console.log("started");
	} else {
		var buttons = $(".register-button");
		
		for(var i = 0; i < buttons.length; i++) {
			buttons[i].disabled = true;
		}
	}
});