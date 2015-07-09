<canvas id="#myChart"></canvas>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js" type="text/javascript"></script>

// Get the context of the canvas element we want to select
var ctx = document.getElementById("myChart").getContext("2d");
var myNewChart = new Chart(ctx).PolarArea(data);
// Get context with jQuery - using jQuery's .get() method.
var ctx = $("#myChart").get(0).getContext("2d");
// This will get the first returned node in the jQuery collection.
var myNewChart = new Chart(ctx);

	jQuery('.chart-input').off().on('input change', function () {
        var property = jQuery(this).data('property');
        var target = chart;
        var value = Number(this.value);
        chart.startDuration = 0;

        if (property == 'innerRadius') {
            value += "%";
        }

        target[property] = value;
        chart.validateNow();
    });

    var data = {
        labels: ["Democrat", "Republican", "Other"],
        datasets: [
            {
                label: "Predicted Leanings",
                fillColor: "rgba(220,220,220,0.2)",
                strokeColor: "rgba(220,220,220,1)",
                pointColor: "rgba(220,220,220,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,220,220,1)",
                data: [70, 80, 90]
            }
        ]
    };
    var context = $("#myChart").get(0).getContext("2d");
    var myNewChart = new Chart(context);
    var myRadarChart = new Chart(context).Radar(data);