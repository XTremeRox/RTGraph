var ctx = $('#canvas');
var plot_used = '/GLASS_BOX -> 98:D3:37:00:BB:8B/default/Pollution Data';
//var data = [1,2,3,4,5];
var config = {
    type: 'line',
    data: {
        datasets: [{
            label: 'CO2 Sensor Data',
            fill: false,
            borderColor: window.chartColors.red,
            backgroundColor: window.chartColors.red,
            data: []
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: plot_used
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
                    labelString: 'ppb'
                }
            }]
        }
    }
};
var myChart = new Chart(ctx, config);