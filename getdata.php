<?php
$str_time = $_GET['strtime'];
$end_time = $_GET['endtime'];
$sensor_id = $_GET['sensorid'];

$get_data = file_get_contents('https://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id='.$sensor_id.'&token=Rj9LEtwnmFfparBkSq3coy7l&start_date=1561001217&end_date=1561001577');
//$get_data = file_get_contents('https://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id='.$sensor_id.'&token=Rj9LEtwnmFfparBkSq3coy7l&start_date='.$str_time.'&end_date='.$end_time);
echo $get_data;
//$response = json_decode($get_data, true);
// $errors = $response['response']['errors'];
// $data = $response['response']['data'][0];
// $url = 'http://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id=5139&token=Rj9LEtwnmFfparBkSq3coy7l&start_date=1558109410&end_date=1564665517';
// //  Initiate curl
// $ch = curl_init();
// // Will return the response, if false it print the response
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// // Set the url
// curl_setopt($ch, CURLOPT_URL,$url);
// // Execute
// $result=curl_exec($ch);
// // Closing
// curl_close($ch);

// // Will dump a beauty json :3
//var_dump(json_decode($response, true));
?>