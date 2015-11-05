/**************titanic***********/
// Pops up a modal with more information.
    $('#farePriceInfo').on('click', function () {
        bootbox.alert("In 1910, a first class cruise ticket was between $240 and $570, third class was around $20 and $40, and second was anywhere in between. Though fare price and accomodation class is often correlated, you may choose to experiment with the numbers to see the significance that fare price might have had regardless of accomodation class.");
    });

    $('#accommodationClassInfo').on('click', function () {
        bootbox.alert("If you were to go on a cruise today, what passenger class would you most likely travel? Try to play around and see what significance your accommodation class might have to do with your survival. Hint: 1st class cabins were situated near life vessels while most of 3rd class was below sea level.");
    });
/**************bike sharing***********/
    // Bootbox.js alert initiations.
    $('#timepickerInfo').on('click', function () {
        bootbox.alert("<p class='font-size18'>Derives Month, Season, Weekday/Weekend, Hour</p>");
    });
    $('#weatherInfo').on('click', function () {
        bootbox.alert(
            "<p class='font-size18'><b>Clear:</b> Clear, Few clouds, Partly cloudy, Partly cloudy</p>"
            + "<p class='font-size18'><b>Moderate:</b> Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist</p>"
            + "<p class='font-size18'><b>Severe:</b> Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds</p>"
        );
    });