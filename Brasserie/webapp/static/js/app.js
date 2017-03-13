$(document).ready(function() {
	var socket = io.connect('http://' + document.domain + ':' + location.port + '/connect')
	socket.on("connected", function() {
		$("#log").append("<p>Connection to "+document.domain+':'+location.port+ " established!</p>");
	});
});


