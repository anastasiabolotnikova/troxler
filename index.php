<?php 

$size = '30px'; 
$blur = '15px'; // it doesn't work in Firefox
$distance = '160px'; 
$color = 'blue'; 

echo '<style>

.fixPoint {
    position: relative;
    height:5px;
    width:5px;
    padding: 20%;
    margin: 0 auto 0 auto;
    top: 5% <!-- Location now is quite silly, to be improved-->
}

.fixPoint:before {
    position: absolute;
    height: 5px;
    width: 5px;
    border-radius: 250px;
    background: black;
    content: "";
}

.circle {
    width:'.$size.';
    height:'.$size.';
    background-color: '.$color.';
    border-radius: 250px;
    display: block;
    position: absolute;
    overflow: hidden;
    top: 50%;
    left: 50%;
    margin: -15px;
    -webkit-filter: blur('.$blur.')
}';

for ($i = 0; $i <= 330; $i+=30) {
    echo '.c'.$i.' { transform: rotate('.$i.'deg) translate('.$distance.'); }';
}

echo 'h1 {text-align:center;font-family:"Lucida Sans Unicode", "Lucida Grande", sans-serif}
</style>

<html>
	
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=windows-1252">
        <script type="text/javascript" src="prefixfree.min.js"></script>
		<title>Toxler Test Environment</title>
	</head>

		<body>
        <h1>Welcome to the Toxler Effect Test Environment</h1>
		<div class="fixPoint">
			<div class="circle c0"></div>
			<div class="circle c30"></div>
			<div class="circle c60"></div>
			<div class="circle c90"></div>
			<div class="circle c120"></div>
			<div class="circle c150"></div>
			<div class="circle c180"></div>
			<div class="circle c210"></div>
			<div class="circle c240"></div>
			<div class="circle c270"></div>
			<div class="circle c300"></div>
			<div class="circle c330"></div>
		</div>
		</body>
</html>';
?>