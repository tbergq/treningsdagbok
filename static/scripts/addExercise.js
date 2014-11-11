
$(document).ready(function(){
	
	$.ajax({
		url : '/programs/show_day/' + day_id,
		type : 'GET',
		/*data : {day_id : day_id} */
	}).done(function(data){
		$("#partial").html(data);
	}); 
	
});