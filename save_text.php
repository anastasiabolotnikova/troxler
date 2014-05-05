<?php

$file = 'saved_data.txt';
// Open the file to get existing content
$current = file_get_contents($file);
// Append a new person to the file

if(isset($_POST['size']) or isset($_POST['dist']) or isset($_POST['blur']) or isset($_POST['color']) or isset($_POST['time'])){
	if($_POST['size']==null){
		$size = 30;
	} else {
		$size = $_POST['size'];
	}
	if($_POST['dist']==null){
		$dist = 160;
	} else {
		$dist = $_POST['dist'];
	}
	if($_POST['blur']==null){
		$blur = 10;
	} else {
		$blur = $_POST['blur'];
	}
	if($_POST['color']==null){
		$color = 'blue';
	} else {
		$color = $_POST['color'];
	}
	if($_POST['time']==null){
		$time = '0000';
	} else {
		$time = $_POST['time'];
	}
	$current .= $size."\t".$dist."\t".$blur."\t".$color."\t".$time.PHP_EOL;
}
else{
	$current .= "FUCK 10\t160\t5\tblue\t0000".PHP_EOL;;
}
// Write the contents back to the file
file_put_contents($file, $current);
?>