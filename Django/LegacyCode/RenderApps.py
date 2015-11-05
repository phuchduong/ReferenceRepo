# Renders the event hub sender page
#from django.contrib.auth.decorators import login_required
#@login_required
def renderEventHubSender(request):
    context = loadApps()
    return render(request, 'azure_models/event-hub-sender.html', context)

def renderTwitterStreamBroker(request):
    context = loadApps()
    return render(request, 'azure_models/twitter-stream-broker.html', context)

def renderCreditCardStreamer(request):
    context = loadApps()
    return render(request, 'azure_models/credit-card-streamer.html', context)