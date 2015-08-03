$('.eventHubHelp').on('click', function () {
    bootbox.dialog({
        message: "<iframe src='{% static 'azure_models\pdf\EventHubGuide.pdf' %}' allowfullscreen width='550' height='400'>",
        title: "Event Hub Help",
        buttons: {
            success: {
                label: "Okay",
                className: "btn-success"
            }
        }
    });
});