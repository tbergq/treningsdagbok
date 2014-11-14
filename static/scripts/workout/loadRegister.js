
function loadRegisterPartial(element) {
	var exercise_id = $(element).attr('id');
	console.log(exercise_id);
	$.ajax({
		url : "/workout/register_partial/" + day_id + "/" + exercise_id + "/",
		type : "GET"	
	}).done(function(data){
		$("#registerDiv").html(data);
	}).error(function(data){
		alert(data.status);
	});
}