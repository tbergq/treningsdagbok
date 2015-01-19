
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
		setDropdown(programId);
	});
}

function setDropdown(programValue) {
	var options = $("#programDropdown").find("option");
	for(var i = 0; i < options.length; i++) {
		if(option[i].value == programValue) {
			alert(option[i]);
			break;
		}
	}
}