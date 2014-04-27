var start = null;

function timeStart(){
	start = new Date().getTime();
	document.getElementById('butt').onclick = function(){(timeStop())};
	document.getElementById('butt').value = "Stop";
}

function timeStop(){
	var stop = new Date().getTime();
	var diff = stop - start;
	var s = parseInt(diff, 10);
	
	//document.write(start);
	//document.write(stop);
	document.getElementById('timeHere').innerHTML = s;
	document.getElementById('butt').onclick = function(){(timeStart())};
	document.getElementById('butt').value = "Start";
}