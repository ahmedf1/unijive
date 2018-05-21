var url = window.location.href;
var queryUser = sliceUrl(url, url.indexOf("?")+1, url.indexOf("&")+1);
var user = sliceUrl(queryUser, queryUser.indexOf("=")+1, queryUser.length+1);
var queryRoom = sliceUrl(url, url.indexOf("&")+1, url.length+1);
var ws = new WebSocket("ws://"+location.host+"/chat_page/?"+queryUser+"&"+queryRoom);
ws.onmessage = function(e){
  insertMessage(JSON.parse(e.data));
}

var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

function sliceUrl(url, index1, index2){
  var query = url.slice(index1, index2-1);
  return query;
}

$(window).load(function() {
  $messages.mCustomScrollbar();
  // setTimeout(function() {
  //   fakeMessage();
  // }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

// function setDate(){
//   d = new Date()
//   if (m != d.getMinutes()) {
//     m = d.getMinutes();
//     $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
//   }
// }

function insertMessage(msg) {
  if ($.trim(msg) == '') {
    return false;
  }
  if(msg.username === user){
    $('<div class="message message-personal">' + msg.text + '</div>').appendTo($('.mCSB_container')).addClass('new');
    $('.message-input').val(null);
    updateScrollbar();
  }
  else{
    $('<div class ="messageButtons" ><div class="message new"><figure class="avatar"><img src="http://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80_4.jpg" /></figure>' + msg.text + '</div><button class = "reactButtons" data-toggle="button" aria-pressed="false">&#x2605</button><button class = "reactButtons" data-toggle="button" aria-pressed="false">&#x1f44d</button><button class = "reactButtons"data-toggle="button" aria-pressed="false">&#x2691</button></div>').appendTo($('.mCSB_container')).addClass('new');
    updateScrollbar();
  }
  // setDate();
  // setTimeout(function() {
  //   fakeMessage();
  // }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  msg = $('.message-input').val();
  ws.send(msg);
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    msg = $('.message-input').val();
    ws.send(msg);
    return false;
  }
})

// var Fake = [
//   'Hi there, I\'m Fabio and you?',
//   'Nice to meet you',
//   'How are you?',
//   'Not too bad, thanks',
//   'What do you do?',
//   'That\'s awesome',
//   'Codepen is a nice place to stay',
//   'I think you\'re a nice person',
//   'Why do you think that?',
//   'Can you explain?',
//   'Anyway I\'ve gotta go now',
//   'It was a pleasure chat with you',
//   'Time to make a new codepen',
//   'Bye',
//   ':)'
// ]

// function fakeMessage() {
//   if ($('.message-input').val() != '') {
//     return false;
//   }
//   $('<div class="message loading new"><figure class="avatar"><img src="http://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80_4.jpg" /></figure><span></span></div>').appendTo($('.mCSB_container'));
//   updateScrollbar();
//
//   setTimeout(function() {
//     $('.message.loading').remove();
//     $('<div class ="messageButtons" ><div class="message new"><figure class="avatar"><img src="http://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80_4.jpg" /></figure>' + Fake[i] + '</div><button class = "reactButtons" data-toggle="button" aria-pressed="false">&#x2605</button><button class = "reactButtons" data-toggle="button" aria-pressed="false">&#x1f44d</button><button class = "reactButtons"data-toggle="button" aria-pressed="false">&#x2691</button></div>').appendTo($('.mCSB_container')).addClass('new');
//     setDate();
//     updateScrollbar();
//     i++;
//   }, 1000 + (Math.random() * 20) * 100);
//
// }
