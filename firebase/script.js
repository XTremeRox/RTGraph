var color = Chart.helpers.color;
var flow1data = [];
var flow2data = [];
var config = {
    type: 'line',
    data: {
        datasets: [{
            label: 'Flow_1',
            backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
            borderColor: window.chartColors.red,
            fill: false,
            data: flow1data
        }, {
            label: 'Flow_2',
            backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
            borderColor: window.chartColors.blue,
            fill: false,
            data: flow2data
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Realtime Sensor Data'
        },
        scales: {
            xAxes: [{
                type: 'time',
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Time'
                },
                ticks: {
                    major: {
                        fontStyle: 'bold',
                        fontColor: '#FF0000'
                    }
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'ppb'
                }
            }]
        }
    }
};

window.onload = function() {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
    var sensor_1= '5139';
    var sensor_2= '3246';
    var dt = new Date();
    dt.setMinutes(dt.getMinutes() - 5);
    var cdt = new Date();
    var obj;
    $.get('getdata.php',{sensorid:sensor_2, strtime : Math.floor(dt.getTime()/1000), endtime : Math.floor(cdt.getTime()/1000)}, function(response) {
        obj = JSON.parse(response);
        //$("#mydata").html(obj);
        for (index=0; index<obj.measures.length;index++){
            flow1data.push({x : index*100+index*10 ,y : obj.measures[index].pollutants.pm10.value})
        }
    });
    $.get('getdata.php',{sensorid:sensor_1, strtime : Math.floor(dt.getTime()/1000), endtime : Math.floor(cdt.getTime()/1000)}, function(response) {
        obj = JSON.parse(response);
        //$("#mydata").html(obj);
        for (index=0; index<obj.measures.length;index++){
            flow2data.push({x : index*100+index*10 ,y : obj.measures[index].pollutants.pm10.value})
        }
    });
    
   // window.myLine.update();
};

document.getElementById('addData').addEventListener('click', function() {
    if (config.data.datasets.length > 0) {
        config.data.datasets[0].data.push({
            x: newDateString(config.data.datasets[0].data.length + 2),
            y: randomScalingFactor()
        });
        config.data.datasets[1].data.push({
            x: newDate(config.data.datasets[1].data.length + 2),
            y: randomScalingFactor()
        });

        window.myLine.update();
    }
});
