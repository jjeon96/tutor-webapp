$(document).ready(function(){
	$('.timepicker').timepicker({
	    timeFormat: 'h:mm p',
	    interval: 60,
	    minTime: '8',
	    maxTime: '10:00pm',
	    startTime: '8:00am',
	    dynamic: true,
	    dropdown: true,
	    scrollbar: true,



    });



  function timeToInt(time) {
    var arr = time.match(/^(0?[1-9]|1[012]):([0-5][0-9])([APap][mM])$/);
    if (arr == null) return -1;

    if (arr[3].toUpperCase() == 'PM') {
      arr[1] = parseInt(arr[1]) + 12;
    }
    return parseInt(arr[1]*100) + parseInt(arr[2]);
  }

  function checkDates() {
    if (($('#mondaystart').val() == '') || ($('#mondayend').val() == '')) return;

    var start = timeToInt($('#mondaystart').val());
    var end = timeToInt($('#mondayend').val());

    if ((start == -1) || (end == -1)) {
      alert("Start or end time it's not valid");
    }

    if (start > end) {
      alert('Start time should be lower than end time');
    }

  }

  $('#mondaystart').on('change', checkDates);
  $('#mondayend').on('change', checkDates);
});

