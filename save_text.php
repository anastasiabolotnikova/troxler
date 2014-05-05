<?php

//variable to select between text files
$test_subj = '';

//Create data to write

if(isset($_POST['size'])){
	$test_subj = 'size';
	//if parameter 'size' that came from form isn't null, we save it to variable and select text file to write data
	if($_POST['size']!=null){
		$size = $_POST['size'];
	} else {
		$size = 30; //default size
	}
}else if(isset($_POST['dist'])){
	$test_subj = 'dist';
	if($_POST['dist']!=null){
		$dist = $_POST['dist'];
	} else {
		$dist = 160; //default distance
		}
}else if(isset($_POST['blur'])){
	$test_subj = 'blur';
	if($_POST['blur']!=null){
		$blur = $_POST['blur'];
	} else {
		$blur = 10; //default blur
	}
}else if(isset($_POST['color'])){
	$test_subj = 'color';
	if($_POST['color']!=null){
		$color = $_POST['color'];
	} else {
		$color = 'blue'; //default color
	}
} else {
	echo "None of parameters is set!";
}

if(isset($_POST['time'])){
	if($_POST['time']!=null){
		$time = $_POST['time'];
	} else {
		$time = '0000'; //null-time - timer was not started
	}
}else {
	echo "Time fucked up";
}
	
//Writing to file	
echo $test_subj;
$file = 'saved_data_'.$test_subj.'.txt';
// Open the file to get existing content
$current = file_get_contents($file);
//Choosing what to write to the file depending on selected test subject
if($test_subj == 'size'){
	$current .= $size."\t".$time.PHP_EOL;
} else if ($test_subj == 'dist'){
	$current .= $dist."\t".$time.PHP_EOL;
} else if($test_subj == 'blur'){
	$current .= $blur."\t".$time.PHP_EOL;
} else if($test_subj == 'color'){
	$current .= $color."\t".$time.PHP_EOL;
} else {
	echo "Invalid test subject!";
}

// Write the contents back to the file
file_put_contents($file, $current);
?>