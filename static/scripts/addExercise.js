var readyExecuted = false;
var count = 0;

// prepare the data
var url = '/programs/get_base_exercises/';
var source =
{
    datatype: "json",
    id: 'value',
    datafields: [
        { name: 'name'}, {name : 'value'}
        
    ],
    
    url: url
};
var dataAdapter = new $.jqx.dataAdapter(source);

$(document).ready(function(){
	if(!readyExecuted) {
		getFormElement();
		showDay();
		//getBaseExercises();
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
		var htmlData = "";
		for(var i = 0; i < data.length; i++) {
			var element = data[i];
			htmlData += "<div id='" + element.name + "' data-number='" + element.value + "'></div>";
		}
		$("#dropdownValues").html(htmlData);
		
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
	      source : new $.jqx.dataAdapter(source),
	      displayMember : 'name',
	      valueMember : 'value',
	      searchMode : 'containsignorecase'
	    	  
	});
	
	$("#combo-" + count).on('change', function (event) {
		
		var value = $(this).jqxComboBox('val');
		
		var inputId = "#" + $(this).parent().attr('data-number');
		$(inputId).val(value);
		
	});
		 
	
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


