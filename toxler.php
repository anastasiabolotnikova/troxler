<?php echo
'<html>
	
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=windows-1252">
		<link rel="stylesheet" type="text/css" href="style.css" />
        <script type="text/javascript" src="prefixfree.min.js"></script>
		<title>Toxler Test Environment</title>
	</head>

		<body>
        <h1>Welcome to the Toxler Effect Test Environment</h1>
		<div class="toxler"> <div class="fixPoint"></div>';
			//<?php
			if (isset($_POST['blur']) and isset($_POST['size']) and isset($_POST['blur']) and isset($_POST['color'])){
				// not predefined param-s
				$distance = $_POST['dist'];
				$size = $_POST['size'];
				$blur = $_POST['blur'];
				$color = $_POST['color'];
			}
			else if(isset($_POST['blur'])){ 
				// testing blurriness impact
				$distance = 160;
				$size = 30;
				$blur = $_POST['blur'];
				$color = "blue";
			} 
			// testing color impact
			else if (isset($_POST['color'])){
				$distance = 160;
				$size = 30;
				$blur = 15;
				$color = $_POST['color'];
			} 
			// testing size impact
			else if (isset($_POST['size'])){
				$distance = 160;
				$size = $_POST['size'];
				$blur = 15;
				$color = "blue";
			} 
			// testing distance impact
			else if (isset($_POST['dist'])){
				$distance = $_POST['dist'];
				$size = 30;
				$blur = 15;
				$color = "blue";
			} 
			// Default param-s
			else {
				$distance = 160;
				$size = 30;
				$blur = 10;
				$color = 'blue';
			}
			//$step = $size/($distance/90);
			for ($i = 0; $i < 360; $i+=30) {
				echo '<div class="circle" style="transform: rotate('.$i.'deg) translate('.$distance.'px);
				width: '.$size.'px; height: '.$size.'px; -webkit-filter: blur('.$blur.'px);
				background-color: '.$color.';" ></div>';
			}
		
		echo
		'</div>
		</body>
</html>';