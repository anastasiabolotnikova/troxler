<?php

$size = $_POST['size'];
$dist = $_POST['dist'];
$blur = $_POST['blur'];
$color = $_POST['color'];
$time = $_POST['time'];

$file = 'test_data.txt';
// Open the file to get existing content
$current = file_get_contents($file);
// Append a new person to the file

if(isset($size) and isset($dist) and isset($blur) and isset($color) and isset($time)){
	if($size==null){
		$size = 10;
	}
	if($dist==null){
		$dist = 160;
	}
	if($blur==null){
		$blur = 5;
	}
	if($color==null){
		$color = 'blue';
	}
	if($time==null){
		$time = '0000';
	}
	$current .= $size."\t".$dist."\t".$blur."\t".$color."\t".$time.PHP_EOL;
}
else{
	$current .= "10\t160\t5\tblue\t0000".PHP_EOL;;
}
// Write the contents back to the file
file_put_contents($file, $current);
?>