$(document).ready(function(){
			
			var ex_id = $("#id_day_excersice").val();
			
			$("#partialForm").attr('action', "/workout/register_partial/" + day_id + "/" + ex_id + "/");

			$("#partialForm").on('submit', function(e) {
				e.preventDefault();
				console.log("yo!!!!");
				$.ajax({
					url : $("#partialForm").attr('action'),
					type : "POST",
					data : $("#partialForm").serialize()
				}).done(function(data) {
					$("#registerDiv").html(data);
				});
			});
		});