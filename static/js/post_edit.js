$(document).ready(function(){
	$('.timepicker').timepicker({
	    timeFormat: 'h:mm p',
	    interval: 60,
	    minTime: '8',
	    maxTime: '10:00pm',
	    startTime: '8:00am',
	    dynamic: true,
	    dropdown: true,
	    scrollbar: true
	});
});

