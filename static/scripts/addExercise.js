var readyExecuted = false;
var count = 0;
var url = '/programs/get_base_exercises/';
// prepare the data
var source = ["katt", "hund"];

$(document).ready(function(){
	if(!readyExecuted) {
		getFormElement();
		showDay();
		readyExecuted = true;
		
	}
	//loadMuscleGroups()
});

function getFormElement() {
	console.log(count);
	$.ajax({
		url: exercisePartialUrl,
		type : "GET",
		data : {program_id : programId, count : count}
	}).done(function(data) {
		if(count == 0) {
			$("#formElements").html(data);
			count;
		} else {
			$("#next-" + count).html(data);
		}
		initializeCombobox();
		
	});
	//count++;
}

function getBaseExercises() {
	
	$.ajax({
		url : '/programs/get_base_exercises/',
		type : "GET",
	}).done(function(data) {
		
		return data;
	});
	
}

$("#muscleGroupDropdown").change(function(){
	
});

function initializeCombobox() {
	for(var i = 0; i <= count; i ++) {
		
	$("#combo-" + count).jqxComboBox({
	      theme: 'energyblue',
	      width: '200px',
	      height: '25px',
	      selectedIndex: 0,
	      autoComplete: true,
	      source : source,
	  });
	}
	//$("#select-" + count).jqxComboBox('loadFromSelect', 'select');
	count++;
}

function showDay() {
	$.ajax({
		url : '/programs/show_day/' + day_id,
		type : 'GET',
		/*data : {day_id : day_id} */
	}).done(function(data){
		$("#partial").html(data);
	});
}


