var start = null;

function timeStart(){
	start = new Date().getTime();
	document.getElementById('timeHere').innerHTML = "0000";
	document.getElementById('butt').onclick = function(){(timeStop())};
	document.getElementById('butt').value = "Stop";

}
var sel_time = null;
function timeStop(){
	var stop = new Date().getTime();
	var diff = stop - start;
	var s = parseInt(diff, 10);
	sel_time = s;
	
	document.getElementById('timeHere').innerHTML = s;
	document.getElementById('butt').onclick = function(){(timeStart())};
	document.getElementById('butt').value = "Start";
}
var sel_size = null;
var sel_dist = null;
var sel_blur = null;
var sel_color = null;

function prepareVars() {
    sel_size = $('#sel_size').val();
	sel_dist = $('#sel_dist').val();
	sel_blur = $('#sel_blur').val();
	sel_color = $('#sel_color').val();
}

function saveData(){
	$.ajax({
        url:        'save_text.php',
        type:       'POST',
        dataType:   'json',
        data:       { size: sel_size, dist: sel_dist, blur: sel_blur, color: sel_color, time: sel_time },
        success:    function(data) {
            alert("Changes saved");
        }
    });
}
