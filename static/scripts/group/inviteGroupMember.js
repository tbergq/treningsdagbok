
$(document).ready(function(){
	$("button").click(function(){
		$.ajax({
			url : '/group/invite/',
			type : "GET",
			data : {group_id : $(this).attr('data-id')},
		}).done(function(data){
			$(".modal-body").html(data);
			$(".modal-footer").html('');
			$("#myModal").modal('show');
		});
	})
});