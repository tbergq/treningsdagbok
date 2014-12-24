$(document).ready(function() {

    

    $('#calendar').fullCalendar({
    	header : {
    	    left:   'title',
    	    center: '',
    	    right:  'today prev,next'
    	},
    	buttonText: {
			today : "I dag"
        },
        monthNames : 
			['Januar', 'Februar', 'Mars', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Desember'],
		firstDay :1,
		dayNamesShort : 
			['Søn', 'Man', 'Tirs', 'Ons', 'Tors', 'Fre', 'Lør'],
		events : '/workout/get_calendar_events/',
		eventClick: function(calEvent, jsEvent, view) {

	        $.ajax({
		        url : "/workout/show_workout/" + calEvent.id + "/",
		        type : "GET",
		        }).done(function(data){
					document.open();
					document.write(data);
					document.close();
			    });

	    },
    });

});