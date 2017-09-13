$(document).ready(function(){
    var tutorAvailTime = [];
    var numOfTimeObjects = 0;
    // $('.postedit_time').hide();



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

  function validateTime(startTime, endTime) {
      if ((startTime == -1) || (endTime == -1)) {
      alert("Start or end time it's not valid");
    }

    if (startTime > endTime) {
      alert('Start time should be lower than end time');
    }
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

      $(".tutor_time_edit").hide();
      $(".tutor_time_delete").hide();
      $(".tutor_time_save").on("click", function() {
          var parentDiv = $(this).parent();
          var parentDivClass = parentDiv.attr("class");
          var startTime = $("#" +startTimeId).val();
          var endTime = $("#"+endTimeId).val();
          var dayOfWeek = $("."+daysofweekClass).val();
          console.log("hello " +  parentDivClass + " start time is " + startTime + " end time is " + endTime);
          validateTime(timeToInt(startTime), timeToInt(endTime));
      });
  });




});

