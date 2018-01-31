


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
    var totalSeconds = timerSecond1 + timerSecond10;

    document.getElementById("hour").disabled=true;
    document.getElementById("minute10").disabled=true;
    document.getElementById("minute1").disabled=true;
    document.getElementById("sec1").disabled=true;
    document.getElementById("sec10").disabled=true;
   

}

function stopTimer(){
    document.getElementById("hour").disabled=false;
    document.getElementById("minute10").disabled=false;
    document.getElementById("minute1").disabled=false;
    document.getElementById("sec1").disabled=false;
    document.getElementById("sec10").disabled=false; 
}


var countDownDate = new Date("Jan 26, 2018 23:58:00").getTime();

// Update the count down every 1 second

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
