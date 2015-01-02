$(document).ready(function(){
	$(".show-day").click(function(){
		$.ajax({
			url : '/programs/show_day/' + $(this).attr('data-id') + "/",
			type : "GET",
			data : {hideEditDelete : false}
		}).done(function(data){
			$(".modal-body").html(data);
			
			$("#myModal").modal('show');
		});
	});
});