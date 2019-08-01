<!DOCTYPE html>
<?php
/**
* A webpage to show Sensor data for a specific time period
* @author Soren.in
* @note The webpage may show only one Flow on account on overlapping information
*/
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>PM10 Pollutant</title>
	<script src="src/jquery.min.js"></script>
	<script src="bootstrap/js/bootstrap.min.js"></script>
	<script src="src/moment.min.js"></script>
	<script src="src/utils.js"></script>
	<script src="src/Chart.min.js"></script>
	<link rel="stylesheet" href="datepicker/daterangepicker.css">
	<link rel="stylesheet" href="src/Chart.min.css">
	<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
	<style>
		canvas {
			-moz-user-select: none;
			-webkit-user-select: none;
			-ms-user-select: none;
		}
	</style>
</head>
<body>
	<div class="container">
		<?php
		if(isset($_POST['time'])){
			$timestamps = str_replace(' ','', $_POST['time']);
			$dates = explode("-", $timestamps);
			$strdate = $dates[0];
			$enddate = $dates[1]; 
			$json1 = file_get_contents('https://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id=5139&token=Rj9LEtwnmFfparBkSq3coy7l&start_date='.$strdate.'&end_date='.$enddate);
			$json2 = file_get_contents('https://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id=3246&token=Rj9LEtwnmFfparBkSq3coy7l&start_date='.$strdate.'&end_date='.$enddate);
			?>
			<div class="row">
				<h3>Select time range to plot</h3>
				<div class="col-md-6">
					<form action="pm10.php" method="POST">
						<input type="text" name="time" style="width:50%;display:inline;"  value="" class="form-control">
						<button class="btn btn-primary">Submit</button>
					</form>
				</div>
			</div>
			<br><br>
			<div style="width:100%;">
				<canvas id="canvas"></canvas>
			</div>
			<?php
		}else{
			?>
			<div class="row">
				<h1>Select time range to plot</h1>
				<div class="col-md-6">
					<form action="pm10.php" method="POST">
						<input type="text" name="time" style="width:50%; display:inline;" class="form-control">
						<button class="btn btn-primary">Submit</button>
					</form>
				</div>
			</div>
			<?php
		}
		?>
	</div>
</body>
	<script src="datepicker/daterangepicker.js"></script>
	<script>
		<?php 
		if(isset($_POST['time'])){ 
			echo 'var jsondata1 =\''.$json1.'\';';
			echo 'var obj1 = JSON.parse(jsondata1);' ;
			echo 'var jsondata2 =\''.$json1.'\';';
			echo 'var obj2 = JSON.parse(jsondata2);' ;
		}
		?>
		
		
		$(function() {
			$('input[name="time"]').daterangepicker({
				timePicker: true,
				maxDate: new Date(),
				startDate: moment().subtract(2, 'days'),
				endDate: moment().startOf('hour'),
				locale: {
				format: 'X'
				}
			});
		});
	</script>
    <?php if(isset($_POST['time'])){ 
        echo '<script src="chartshow2.js"></script>';
        echo '<script>$(document).ready(function(){
            for (index=0; index<obj1.measures.length; index++){
                config.data.datasets[0].data.push({
                    x: moment.unix(obj1.measures[index].date),
                    y: obj1.measures[index].pollutants.pm10.value
                });
            }
            for (index=0; index<obj2.measures.length; index++){
                config.data.datasets[1].data.push({
                    x: moment.unix(obj2.measures[index].date),
                    y: obj2.measures[index].pollutants.pm10.value
                });
            }
            // if (config.data.datasets.length > 0) {
            //     config.data.datasets[0].data.push({
            //         x: \'1564520980\',
            //         y: \'10\'
            //     });
            //     config.data.datasets[1].data.push({
            //         x: \'1564691400\',
            //         y: \'15\'
            //     });
            
                myChart.update();
            //}
        });</script>';
    } ?>
</html>