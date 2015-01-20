
function loadRequestedProgram() {
	var programId = $("#programDropdown").val();
	$.ajax({
		url: '/workout/registered_workouts/',
		data : {program_id : programId},
		type : "GET"
	}).done(function(data){
		document.open();
		document.write(data);
		document.close();
	});
}

