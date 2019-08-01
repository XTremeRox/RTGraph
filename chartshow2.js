var ctx = $('#canvas');
//var data = [1,2,3,4,5];
var config = {
    type: 'line',
    data: {
        datasets: [{
            label: 'Flow 1',
            fill: false,
            borderColor: window.chartColors.red,
            backgroundColor: window.chartColors.red,
            data: []
        }, {
            label: 'Flow 2',
            fill: false,
            borderColor: window.chartColors.green,
            backgroundColor: window.chartColors.green,
            data: []
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Sensor Data'
        },
        scales: {
            xAxes: [{
                type:'time',
                time:{
                    displayFormats: {
                        minute: 'h:mm a'
                    }
                },
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Time'
                },
                ticks: {
                    callback: function(dataLabel, index) {
                        // Hide the label of every 2nd dataset. return null to hide the grid line too
                        return index % 2 === 0 ? dataLabel : '';
                    }
                }
            }],
            yAxes: [{
                display: true,
                beginAtZero: false,
                scaleLabel: {
                    display: true,
                    labelString: 'µg/m3'
                }
            }]
        }
    }
};
var myChart = new Chart(ctx, config);
