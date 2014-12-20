var readyExecuted = false;
var count = 0;

// prepare the data
var url = '/programs/get_base_exercises/';
var source =
{
    datatype: "json",
    datafields: [
        { name: 'name' }
        
    ],
    id: 'id',
    url: url
};
var dataAdapter = new $.jqx.dataAdapter(source);

$(document).ready(function(){
	if(!readyExecuted) {
		getFormElement();
		showDay();
		readyExecuted = true;
		//source = getBaseExercises();
		
	}
	//loadMuscleGroups()
});



function getFormElement() {
	
	$.ajax({
		url: exercisePartialUrl,
		type : "GET",
		data : {program_id : day_id, count : count}
	}).done(function(data) {
		if(count == 0) {
			$("#formElements").html(data);
			
		} else {
			$("#next-" + count).html(data);
		}
		
		initializeCombobox();
		$("#id_form-TOTAL_FORMS").val(count);
		
	});
	//count++;
}

function getBaseExercises() {
	
	$.ajax({
		url : '/programs/get_base_exercises/',
		datatype : "json",
		type : "GET",
	}).done(function(data) {
		console.log(data);
		return data;
	});
	
}

$("#muscleGroupDropdown").change(function(){
	
});

function initializeCombobox() {
	
		
	$("#combo-" + count).jqxComboBox({
	      theme: 'bootstrap',
	      width: '100%',
	      height: '34px',
	      selectedIndex: 0,
	      autoComplete: true,
	      source : dataAdapter,
	      displayMember : 'name',
	      valueMember : 'name'
	});
	
	$("#combo-" + count).on('change', function (event) {
		
		var value = $(this).jqxComboBox('getSelectedIndex');
		var inputId = "#" + $(this).parent().attr('data-number');
		$(inputId).val(value);
		console.log($(inputId).val());
	});
		 
	//$("#combo-" + count).jqxComboBox('loadFromSelect', 'select-' + count);
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


