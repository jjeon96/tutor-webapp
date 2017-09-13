$(document).ready(function(){
    var tutorAvailableTime = [];
    var numOfTimeObjects = 0;
    // $('.postedit_time').hide();

  function convertTimeFormat(str) {
        var time = str;
        var hours = Number(time.match(/^(\d+)/)[1]);
        var minutes = Number(time.match(/:(\d+)/)[1]);
        var AMPM = time.match(/\s(.*)$/)[1];
        if (AMPM == "PM" && hours < 12) hours = hours + 12;
        if (AMPM == "AM" && hours == 12) hours = hours - 12;
        var sHours = hours.toString();
        var sMinutes = minutes.toString();
        if (hours < 10) sHours = "0" + sHours;
        if (minutes < 10) sMinutes = "0" + sMinutes;
        return (sHours + ":" + sMinutes);
  }
  function timeToInt(time) {
    var formatedTime = convertTimeFormat(time);
    var hoursMinutes = formatedTime.split(/[.:]/);
    var hours = parseInt(hoursMinutes[0], 10);
    var minutes = hoursMinutes[1] ? parseInt(hoursMinutes[1], 10) : 0;
    var convertedTime = (hours + minutes / 60);

    if (convertedTime == null) return -1;

    return convertedTime;
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

  //need a valid work flow for alerting
  function validateTime(startTime, endTime) {
      console.log("start Time is " + startTime);
      console.log("end Time is " + endTime);
      if ((startTime == -1) || (endTime == -1)) {
      alert("Start or end time it's not valid");
      return false;
    }

    if (startTime > endTime) {
      alert('Start time should be lower than end time');
      return false;
    }
      return true;
  }

  $(".add_tutor_time").on('click',function() {
      numOfTimeObjects++;
      var domClass = "avail_time" + numOfTimeObjects;
      var startTimeId = "time_start_" + numOfTimeObjects;
      var endTimeId = "time_end_" + numOfTimeObjects;
      var daysofweekClass = "daysofweek" + numOfTimeObjects;
      $("#Availability").append("<div class='" + domClass + "'>" +
                        "<label><input type='text' value='Day of Week' class='"+daysofweekClass+"'></label>" +
                        "<input class='timepicker text-center'  jt-timepicker='' time='model.time' time-string='model.timeString' default-time='model.options.defaultTime' time-format='model.options.timeFormat' start-time='model.options.startTime' min-time='model.options.minTime' max-time='model.options.maxTime' interval='model.options.interval' dynamic='model.options.dynamic' scrollbar='model.options.scrollbar' dropdown='model.options.dropdown' placeholder='start time' id = '"+startTimeId+"'>" +
                        "<input class='timepicker text-center' jt-timepicker='' time='model.time' time-string='model.timeString' default-time='model.options.defaultTime' time-format='model.options.timeFormat' start-time='model.options.startTime' min-time='model.options.minTime' max-time='model.options.maxTime' interval='model.options.interval' dynamic='model.options.dynamic' scrollbar='model.options.scrollbar' dropdown='model.options.dropdown' placeholder='end time' id = '"+endTimeId+"'>" +
                        "<button class='tutor_time_save'>Save</button>"+
                        "<button class='tutor_time_edit'>Edit</button>"+
                        "<button class='tutor_time_delete'>Delete</button>"+
                        "<div><br>");
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

      //made it for now
      $(".tutor_time_edit").hide();
      $(".tutor_time_delete").hide();
      //code for creating a time object,
      //currently contains a bug, may need a different workflow
      $(".tutor_time_save").on("click", function() {
          var parentDiv = $(this).parent();
          var parentDivClass = parentDiv.attr("class");
          var startTime = $("#" +startTimeId).val();
          var endTime = $("#"+endTimeId).val();
          var dayOfWeek = $("."+daysofweekClass).val();

          if (validateTime(timeToInt(startTime), timeToInt(endTime))) {
              var timeObject = {"startTime": startTime,
                                "endTime": endTime,
                                "dayOfWeek": dayOfWeek}
              tutorAvailableTime.push(timeObject);
            // console.log("hello " +  parentDivClass + " start time is " + startTime + " end time is " + endTime);
              console.log(tutorAvailableTime);
          } else {
              console.log("Time Validation has failed");
          }
      });
  });




});

