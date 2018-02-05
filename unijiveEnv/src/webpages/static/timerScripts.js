


// Set the date we're counting down to



function settingTimer(){
    var timerHour = document.getElementById('hour').value;
    if(!timerHour){timerHour = 0;}

    var timerMinute10 = document.getElementById("minute10").value;
    if(!timerMinute10){timerMinute10 = 0;}

    var timerMinute1 = document.getElementById("minute1").value;
    if(!timerMinute1){timerMinute1 = 0;}

    var timerSecond1 = document.getElementById("sec1").value;
    if(!timerSecond1){timerSecond1 = 0;}

    var timerSecond10 = document.getElementById("sec10").value;
    if(!timerSecond10){timerSecond10 = 0;}

    var totalMinutes = timerMinute10 + timerMinute1;
    if(totalMinutes<10){totalMinutes = ("0" + totalMinutes).slice(-2);}

    var totalSeconds = timerSecond1 + timerSecond10;
    if(totalSeconds<10){totalSeconds = ("0" + totalSeconds).slice(-2);}
/*
    alert(timerHour);
    alert(totalMinutes);
    alert(totalSeconds);
    */



    document.getElementById("hour").disabled=true;
    document.getElementById("minute10").disabled=true;
    document.getElementById("minute1").disabled=true;
    document.getElementById("sec1").disabled=true;
    document.getElementById("sec10").disabled=true;

    

            // min/hr * sec/min * ms/sec
    var sum = (timerHour * 60 * 60 * 1000) + (totalMinutes * 60 * 1000) + (totalSeconds * 1000);
    var deadline = new Date(Date.parse(new Date()) + sum);
    cancelled = false;
    initializeClock(deadline);

   

}

function stopTimer(){
    cancelled = true;
    // resetting values
    document.getElementById("hour").value=0;
    document.getElementById("minute10").value=0;
    document.getElementById("minute1").value=0;
    document.getElementById("sec1").value=0;
    document.getElementById("sec10").value=0; 

    // allowing input again
    document.getElementById("hour").disabled=false;
    document.getElementById("minute10").disabled=false;
    document.getElementById("minute1").disabled=false;
    document.getElementById("sec1").disabled=false;
    document.getElementById("sec10").disabled=false; 

    
}


function getTimeRemaining(deadline) {
    var t = Date.parse(deadline) - Date.parse(new Date());
    var seconds1 = Math.floor(((t / 1000) % 60) / 10);
    var seconds10 = Math.floor(((t / 1000) % 60) % 10);
    var minutes10 = Math.floor(((t / 1000 / 60) % 60) / 10);
    var minutes1 = Math.floor(((t / 1000 / 60) % 60) % 10);
    var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
    return {
      'total': t,
      'hours': hours,
      'minutes10': minutes10,
      'minutes1': minutes1,
      'seconds1': seconds1,
      'seconds10': seconds10,
    };
  }
  
  var cancelled = false;


var countDownDate = new Date("Jan 26, 2018 23:58:00").getTime();

  
  function initializeClock(endtime) {
    var hourSpan = document.getElementById("hour");
    var minute10Span = document.getElementById("minute10");
    var minute1Span = document.getElementById("minute1");
    var sec1Span = document.getElementById("sec1");
    var sec10Span = document.getElementById("sec10"); 

  
    function updateClock() {
      var t = getTimeRemaining(endtime);
  
      
      hourSpan.value = (t.hours);
      minute10Span.value = (t.minutes10);
      minute1Span.value = (t.minutes1);
      sec1Span.value = (t.seconds1);
      sec10Span.value = (t.seconds10);
  
      if (t.total <= 0) {
        clearInterval(timeinterval);
      }

      if(cancelled){clearInterval(timeinterval);}
    }
  
    updateClock();
    var timeinterval = setInterval(updateClock, 1000);
  }
  
  

  // Update the count down every 1 second
/*
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    
    // Find the distance between now an the count down date
    var distance = countDownDate - now;
    
    // Time calculations for days, hours, minutes and seconds
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = hours + ":"
    + minutes + ":" + seconds;
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "EXPIRED";
    }
}, 1000);

*/