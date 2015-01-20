$(document).ready(
		function() {

			var ex_id = $("#id_day_excersice").val();

			$("#partialForm").attr('action',
					"/workout/register_partial/" + day_id + "/" + ex_id + "/");

			$("#partialForm").on('submit', function(e) {
				e.preventDefault();
				$("#submitPartialButton").attr('disabled', true);
				$.ajax({
					url : $("#partialForm").attr('action'),
					type : "POST",
					data : $("#partialForm").serialize()
				}).done(function(data) {
					$("#registerPartial").html(data);
				});
			});
			//getPreviousSetData(ex_id);
			//getPreviousLifted(ex_id);
			$("#submitPartialButton").attr('disabled', false);
			
			
		});


function getPreviousSetData(id) {
	$.ajax({
		url : "/workout/get_previous_register_data/" + id + "/",
		type : "GET",
		
	}).done(function(data){
		$("#previousDiv").html(data);
		
	});
}

function getPreviousLifted(id) {
	$.ajax({
		url: "/workout/previous_lifted/" + id + "/",
		type : "GET"
	}).done(function(data){
		$("#previousLiftedDiv").html(data);
		
	})
}


