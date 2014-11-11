
function pala(element) {
	console.log("pala");
	var id = $(element).attr('id');
	var span = $(element).find("span");
	if(span.hasClass("glyphicon-expand")) {
		span.removeClass("glyphicon-expand");
		span.addClass("glyphicon-collapse-down");
		$("." + id).removeClass("hidden");
	} else {
		console.log("else");
		span.removeClass("glyphicon-collapse-down");
		span.addClass("glyphicon-expand");
		$("." + id).addClass("hidden");
	}
}