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

function prepareSize() {
    sel_size = $('#sel_size').val();
}
function prepareDist() {
	sel_dist = $('#sel_dist').val();
}
function prepareBlur() {
	sel_blur = $('#sel_blur').val();
}
function prepareColor() {
	sel_color = $('#sel_color').val();
}

function saveSize(){
	$.ajax({
        url:        'save_text.php',
        type:       'POST',
        dataType:   'json',
        data:       { size: sel_size, time: sel_time },
        success:    function(data) {
            alert("Changes saved");
        }
    });
}
function saveDist(){
	$.ajax({
        url:        'save_text.php',
        type:       'POST',
        dataType:   'json',
        data:       { dist: sel_dist, time: sel_time },
        success:    function(data) {
            alert("Changes saved");
        }
    });
}
function saveBlur(){
	$.ajax({
        url:        'save_text.php',
        type:       'POST',
        dataType:   'json',
        data:       { blur: sel_blur, time: sel_time },
        success:    function(data) {
            alert("Changes saved");
        }
    });
}
function saveColor(){
	$.ajax({
        url:        'save_text.php',
        type:       'POST',
        dataType:   'json',
        data:       { color: sel_color, time: sel_time },
        success:    function(data) {
            alert("Changes saved");
        }
    });
}
