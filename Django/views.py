from django.shortcuts import get_object_or_404, render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
  
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def loadApps():
    from azure_models.models import PredictiveModel, WebApps
    predictive_models_list = PredictiveModel.objects.filter(isEnabled=True).order_by('title')
    webAppsList = WebApps.objects.filter(isEnabled=True).order_by('title')
    context = {'predictive_models_list': predictive_models_list, 'webAppsList': webAppsList }
    return context

# Renders main/home screen.
def index(request):
    #return render(request, 'azure_models/base3.html')
    context = loadApps()
    return render(request, 'azure_models/landing.html',context)

# Renders an app
def renderApp(request, appName):
    context = loadApps()
    try:
        import django
        from django import template
        templateURL = "azure_models/app-" + appName + ".html"
        django.template.loader.get_template(templateURL)
        
        from azure_models.models import WebApps
        webApp = WebApps.objects.get(webAppID=appName)
        context['webApp'] = webApp

        return render(request, templateURL, context)
    except template.TemplateDoesNotExist:
        return render(request, 'azure_models/PageNotFound.html', context)


# renders a webservice demo page given the experiment name.
def render_demo(request, experimentName):
    context = loadApps()
    try:
        from azure_models.models import PredictiveModel
        single_model = PredictiveModel.objects.get(experiment=experimentName)
        context['single_model'] = single_model
        templateURL = 'azure_models/demo-' + single_model.experiment + '.html'
        return render(request, templateURL, context)
    except PredictiveModel.DoesNotExist:
        return render(request, 'azure_models/PageNotFound.html', context)

# renders a self deployed model of a guest.
def render_guest_demo(request, parentExperiment, guestExperimentName):
    context = loadApps()
    try:
        from azure_models.models import GuestML
        from azure_models.models import PredictiveModel
        single_model = GuestML.objects.get(experimentKeyName=guestExperimentName)
        parentExperimentObj = PredictiveModel.objects.get(experiment=parentExperiment)
        single_model.experiment = parentExperiment
        single_model.question = parentExperimentObj.question
        single_model.description = parentExperimentObj.description
        context['single_model'] = single_model
        parentTemplate = "azure_models/demo-" + parentExperiment + ".html"
        return render(request, parentTemplate, context)
    except PredictiveModel.DoesNotExist:
        return render(request, 'azure_models/PageNotFound.html', context)

# Renders the video tutorial page.
def videoTutorials(request):
    context = loadApps()
    return render(request, 'azure_models/video-tutorials.html',context)

#renders the page where people can add their own models using dsd templates
def renderRegisterGuestModel(request, parentExperiment):
    import urllib2
    import json 

    data = request.POST.get('schema')
    data = str(data)
    body = str.encode(data)

    # print data #uncomment for debug

    from azure_models.models import PredictiveModel
    experiment = PredictiveModel.objects.get(experiment=experimentName)
    url = experiment.url
    api_key = experiment.apiKey
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib2.Request(url, body, headers) 
    response = urllib2.urlopen(req)
    result = response.read()
    # print result #uncomment for debug
    return HttpResponse(result)
    #context = loadApps()
    #applicableGuestModels = ['titanic', 'bikesharing']
    #if parentExperiment in applicableGuestModels:
    #    #if the template exists, render it
    #    templateURL = 'azure_models/guest-ml-new.html'
    #    from azure_models.models import PredictiveModel
    #    if parentExperiment == 'titanic':
    #        title = 'Titanic'
    #        schemaRaw = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
    #        schemaUser = ['PassengerClass', 'Gender', 'Age', 'SiblingSpouse', 'ParentChild', 'FarePrice', 'PortEmbarkation']
    #    elif parentExperiment == 'bikesharing':
    #        title = 'Bike Sharing'
    #        schemaRaw = ["season", "holiday", "workingday", "weather", "temp", "atemp", "hum", "windspeed", "hr", "weekday", "mnth", "cnt"]
    #        schemaUser = ["season", "holiday", "workingday", "weather", "temp", "atemp", "humidity", "windspeed", "hour", "weekday", "month", "Count"]
    #    else:
    #        # just for completeness, though this else statement should never be hit.
    #        title = 'Unknown Experiment'
    #        schemaRaw = {}
    #        schemaUser = []
    #    schemaZip = zip(schemaRaw, schemaUser)
    #    parentModelObj = PredictiveModel.objects.get(experiment=parentExperiment)
        
    #    context['parentExperiment'] = {
    #        'title': title, 
    #        'name':parentExperiment, 
    #        'obj': parentModelObj,
    #        'schema': schemaZip
    #    }
    #    context['single_model'] = { "experiment": parentExperiment }
    #    return render(request, templateURL, context)
    #else:
    #    #show 404 if it does not exist.
    #    return render(request, 'azure_models/PageNotFound.html', context)

# Sends a request to the machine learning model in azure
# to receive a prediction.
def make_prediction(request, experimentName):

    import urllib2
    import json 
    
    #print request.POST.get('schema')
    #data = json.load(request.POST.get('schema'))
    
    if request.POST.get('schema'):
        data = request.POST.get('schema')
        data = str(data)
        body = str.encode(data)
    else:
        data = getExperimentJSON(request, experimentName)
        body = str.encode(json.dumps(data))

    # print data #uncomment for debug

    from azure_models.models import PredictiveModel
    experiment = PredictiveModel.objects.get(experiment=experimentName)
    url = experiment.url
    api_key = experiment.apiKey
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib2.Request(url, body, headers) 
    response = urllib2.urlopen(req)
    result = response.read()
    # print result #uncomment for debug
    return HttpResponse(result)


def guest_prediction(request, parentExperiment, guestExperimentName):

    import urllib2
    import json 
    
    if parentExperiment == 'titanic':
        parentSchema = "guesttitanic"
    else:
        parentSchema = parentExperiment

    data = getExperimentJSON(request, parentSchema)
    body = str.encode(json.dumps(data))

    from azure_models.models import GuestML
    experiment = GuestML.objects.get(experimentKeyName=guestExperimentName)
    url = experiment.post_url
    api_key = experiment.apiKey
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    req = urllib2.Request(url, body, headers) 
    response = urllib2.urlopen(req)
    result = response.read()

    #updates the db fields for model usage
    experiment.usageCount += 1

    from datetime import datetime
    experiment.lastUsage = datetime.now()
    experiment.save()

    return HttpResponse(result)


def registerGuestModel(request, parentExperiment):
    #try:
    from azure_models.models import GuestML
    from datetime import datetime
    newEntry = GuestML()
    
    firstName = request.POST.get('firstName').lower()
    lastName = request.POST.get('lastName').lower()
    postURL = request.POST.get('postURL')
    apiKey = request.POST.get('apiKey')
    #parentExperiment = request.POST.get('parentExperiment')
    currentTime = datetime.now()
    GUID = str(currentTime.year)[-2:] + str(currentTime.month) + str(currentTime.day) + str(currentTime.hour) + str(currentTime.minute) + str(currentTime.second)

    newEntry.experimentKeyName = lastName + firstName + GUID
    newEntry.parentExperiment = parentExperiment
    newEntry.title = firstName.title() + " " + lastName.title() + "'s Titanic Survival Predictor"
    newEntry.fname = firstName
    newEntry.lname = lastName
    newEntry.post_url = postURL
    newEntry.apiKey = apiKey
    newEntry.pub_date = currentTime
    newEntry.usageCount = 0
    newEntry.lastUsage = currentTime
    newEntry.isEnabled = True

    newEntry.save()
    return HttpResponse(newEntry.experimentKeyName)
    #except Exception:
    #    return HttpResponse(505)
    
#Gets the feature vector format, and parses the request into the feature vector parameters.
def getExperimentJSON(request, experimentName):
    import json

    data = {
        "Inputs": {
            "input1": {
                
            },
        },
        "GlobalParameters": {}
    } #end of data

    if experimentName=='titanic':
        data['Inputs']['input1'] = {
            "ColumnNames": ["AccommodationClass", "Sex", "Age", "SiblingSpouse", "ParentChild", "Fare", "Embarked"],
            "Values": [ [ 
                request.POST.get('AccommodationClass'), 
                request.POST.get('Sex'), 
                request.POST.get('Age'), 
                request.POST.get('SiblingSpouse'), 
                request.POST.get('ParentChild'), 
                request.POST.get('Fare'), 
                request.POST.get('Embarked') ],]
        }
    elif experimentName=='entityextractor':
        data['Inputs']['input1'] = {
            "ColumnNames": ["Col1"],
                "Values": [
                    [request.POST.get('inputText'),]
                ]
        }
    elif experimentName=='reviewrater':
        data['Inputs']['input1'] = {
            "ColumnNames": ["Col2"],
            "Values": [
                [request.POST.get('inputText'),]
            ]
        }
    elif experimentName=='bikesharing':
        data['Inputs']['input1'] = {
            "ColumnNames": ["season", "holiday", "workingday", "weather", "temp", "atemp", "humidity", "windspeed", "hour", "weekday", "month", "Count"],
            "Values": [ [
                request.POST.get('season'), 
                request.POST.get('holiday'), 
                request.POST.get('workingday'), 
                request.POST.get('weather'), 
                request.POST.get('temp'), 
                request.POST.get('atemp'), 
                request.POST.get('humidity'),
                request.POST.get('windspeed'), 
                request.POST.get('hour'), 
                request.POST.get('weekday'), 
                request.POST.get('month'),
                request.POST.get('count'),
                ],
            ]
        }
    elif experimentName=='caraccidentoutcomepredictor':
        data =  {
            "Id": "score00001",
            "Instance": {
                "FeatureVector": {
                
                },
                "GlobalParameters": {
                }
            }
        }
        data['Instance']['FeatureVector'] = {
            "RushHour": request.POST.get('RushHour'),
            "Alcohol": request.POST.get('Alcohol'),
            "StraightCurved": request.POST.get('StraightCurved'),
            "TowInvolvement": request.POST.get('TowInvolvement'),
            "Workzone": request.POST.get('Workzone'),
            "Weekday": request.POST.get('Weekday'),
            "Interstate": request.POST.get('Interstate'),
            "Lighting": request.POST.get('Lighting'),
            "ImpactSite": request.POST.get('ImpactSite'),
            "Pedestrian": request.POST.get('Pedestrian'),
            "Intersection": request.POST.get('Intersection'),
            "OnRoadway": request.POST.get('OnRoadway'),
            "RoadGrade": request.POST.get('RoadGrade'),
            "SpeedLimit": request.POST.get('SpeedLimit'),
            "RoadCondition": request.POST.get('RoadCondition'),
            "TrafficControlDevice": request.POST.get('TrafficControlDevice'),
            "RoadType": request.POST.get('RoadType'),
            "VehiclesInvolved": request.POST.get('VehiclesInvolved'),
            "Weather": request.POST.get('Weather'),
            "PropertyDamage": request.POST.get('PropertyDamage'),
            "NumberOfLanes": request.POST.get('NumberOfLanes'),
        }
    elif experimentName == 'guesttitanic':
        data['Inputs']['input1'] = {
            "ColumnNames": ["PassengerClass", "Gender", "Age", "SiblingSpouse", "ParentChild", "FarePrice", "PortEmbarkation"],
            "Values": [ [ 
                request.POST.get('AccommodationClass'), 
                request.POST.get('Sex'), 
                request.POST.get('Age'), 
                request.POST.get('SiblingSpouse'), 
                request.POST.get('ParentChild'), 
                request.POST.get('Fare'), 
                request.POST.get('Embarked') ],]
        }
    elif experimentName == 'political-party':
        data['Inputs']['input1'] = {
            "ColumnNames": ["CAND_PTY_AFFILIATION", "CAND_OFFICE", "OCC_GROUP", "NEW_CITY", "NEW_STATE", "TRANS_CUT_AMT"],
            "Values": [ 
                [# payload 1
                    "OTHER", 
                    request.POST.get('candidate'), 
                    request.POST.get('occupation'), 
                    request.POST.get('city'), 
                    request.POST.get('state'), 
                    request.POST.get('contribution')
                ], #end of payload 1
            ] # end of all values
        }
    return data

# Sends data to an event hub.
def stream_tweets_to_hub(request):
    import tweepy
    from tweepy import OAuthHandler
    from tweepy import Stream
    import random
    from random import randint
    import json
    from datetime import datetime
    
    class TwitterStreamListenerFull(tweepy.StreamListener):
        def __init__(self, tweetLimit, eventHubName, namespace, policyName, sasKey):
            super(TwitterStreamListenerFull, self).__init__()
            self.hubClient = EventHubClient(eventHubName, namespace, policyName, sasKey)
            self.hubStatusCode = 201
            self.tweetLimit = int(tweetLimit)
            self.num_tweets = 0
            self.twitterStatusCode = 200
            self.twitterStatusTitle = "OK"
            self.twitterStatusDescription = "Success!"
            self.streamListenerMessage = ""
        def on_status(self, status):
            print(status.text + "inside on status")
            self.twitterStatusCode = status
        def on_data(self, data):
            # Gets a random partition for the event hub to use. Spreads the load of the reader
            # and writer in the event hub.
            partition = str(randint(0,16))

            #encodes it into python 2.XX as ascii [str(data).encode("utf-8") which is the 
            #equivalent to .NET UTF-8. if python 3.XX then str(data).encode("utf-8"). 
            #If C# then GetBytes(Data)
            
            #body = str(data)

            tweetJSON = json.loads(data)

            # converting twitter time to ISO 8061 format
            created_at = tweetJSON['created_at']
            dateTimeObject = datetime.strptime(tweetJSON['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
            tweetJSON['created_at_iso'] = str(dateTimeObject)

            # parsing longitude and latitude
            if tweetJSON['coordinates']:
                if tweetJSON['coordinates']['coordinates']:
                    longlat = tweetJSON['coordinates']['coordinates']
                    #tweetJSON['tweet_longitude'] = longlat[0]
                    #tweetJSON['tweet_latitude'] = longlat[1]
                    #print tweetJSON['tweet_longitude']
                    #print tweetJSON['tweet_latitude']
                    tweetJSON['tweet_long_lat'] = str(longlat[1]) + ", " + str(longlat[0])
                    print tweetJSON['tweet_long_lat']

            body = str(json.dumps(tweetJSON))

            # sends partition and tweet body to azure event hub.
            self.hubStatusCode = self.hubClient.sendMessage(body,partition)
            # post send action success/fail
            if self.hubStatusCode != 201:
                if self.num_tweets == 0:
                    self.streamListenerMessage = "Failed connect to the Azure Event Hub. Please check your Event Hub credentials."
                else:
                    self.streamListenerMessage = "Successfully sent " + str(self.num_tweets) + " Tweet(s) before an error with the Event Hub connection occurred."
                return False
            elif self.num_tweets < self.tweetLimit: # tweet checker
                self.num_tweets += 1
                print "Sent Tweet #" + str(self.num_tweets) + ": " + body[107:169]
                self.streamListenerMessage = "Successfully sent " + str(self.num_tweets) + " Tweet(s) to the Azure Event Hub."
                return True # continue to next weet
            else:
                self.streamListenerMessage = "Successfully sent " + str(self.num_tweets) + " Tweet(s) to the Azure Event Hub."
                return False # stops tweet stream
        def on_error(self, status):
            if status == 304:
                self.twitterStatusTitle = "Not Modified"
                self.twitterStatusDescription = "There was no new data to return."
            elif status == 400:
                self.twitterStatusTitle = "Bad Request"
                self.twitterStatusDescription = "The request was invalid or cannot be otherwise served. An accompanying error message will explain further. In API v1.1, requests without authentication are considered invalid and will yield this response."
            elif status == 401:
                self.twitterStatusTitle = "Unauthorized"
                self.twitterStatusDescription = "Authentication credentials were missing or incorrect.Also returned in other circumstances, for example all calls to API v1 endpoints now return 401 (use API v1.1 instead)."
            elif status == 403:
                self.twitterStatusTitle = "Forbidden"
                self.twitterStatusDescription = "The request is understood, but it has been refused or access is not allowed. An accompanying error message will explain why. This code is used when requests are being denied due to update limits."
            elif status == 404:
                self.twitterStatusTitle = "Not Found"
                self.twitterStatusDescription = "The URI requested is invalid or the resource requested, such as a user, does not exists. Also returned when the requested format is not supported by the requested method."
            elif status == 406:
                self.twitterStatusTitle = "Not Acceptable"
                self.twitterStatusDescription = "Returned by the Search API when an invalid format is specified in the request."
            elif status == 410:
                self.twitterStatusTitle = "Gone"
                self.twitterStatusDescription = "This resource is gone. Used to indicate that an API endpoint has been turned off."
            elif status == 420:
                self.twitterStatusTitle = "Enhance Your Calm"
                self.twitterStatusDescription = "Returned by the version 1 Search and Trends APIs when you are being rate limited."
            elif status == 422:
                self.twitterStatusTitle = "Unprocessable Entity"
                self.twitterStatusDescription = "Returned when an image uploaded to POST account / update_profile_banner is unable to be processed."
            elif status == 429:
                self.twitterStatusTitle = "Too Many Requests"
                self.twitterStatusDescription = "Returned in API v1.1 when a request cannot be served due to the application's rate limit having been exhausted for the resource. See Rate Limiting in API v1.1."
            elif status == 500:
                self.twitterStatusTitle = "Internal Server Error"
                self.twitterStatusDescription = "Something is broken. Please post to the developer forums so the Twitter team can investigate."
            elif status == 502:
                self.twitterStatusTitle = "Bad Gateway"
                self.twitterStatusDescription = "Twitter is down or being upgraded."
            elif status == 503:
                self.twitterStatusTitle = "Service Unavailable"
                self.twitterStatusDescription = "The Twitter servers are up, but overloaded with requests. Try again later."
            elif status == 504:
                self.twitterStatusTitle = "Gateway timeout"
                self.twitterStatusDescription = "The Twitter servers are up, but the request couldn't be serviced due to some failure within our stack. Try again later."
            else:
                self.twitterStatusTitle = "Unknown error"
                self.twitterStatusDescription = "The twitter API has returned an unknown error."
            self.streamListenerMessage = "Successfully sent " + str(self.num_tweets) + "Tweet(s) before error. Error with the Twitter API. Error Code: " + self.twitterStatusCode + " " + self.twitterStatusTitle + ": " + self.twitterStatusDescription
            print self.streamListenerMessage

    # Twitter api keys
    access_token         = request.POST.get('accessToken')
    access_token_secret  = request.POST.get('tokenSecret')
    consumer_token       = request.POST.get('consumerKey')
    consumer_secret      = request.POST.get('consumerSecret')

    # Event Hub Credentials
    eventHubName         = request.POST.get('eventHubName')
    namespace            = request.POST.get('namespace')
    policyName           = request.POST.get('policyName')
    sasKey               = request.POST.get('sasKey')

    # Max tweets to send
    tweetLimit           = int(request.POST.get('tweetLimit'))

    #Authorization
    oAuthHeader         = tweepy.OAuthHandler(consumer_token, consumer_secret)
    tweetStreamListener = TwitterStreamListenerFull(
        tweetLimit,
        eventHubName,
        namespace,
        policyName,
        sasKey
    )
    
    oAuthHeader = OAuthHandler(consumer_token, consumer_secret)
    oAuthHeader.set_access_token(access_token, access_token_secret)

    myAPI = tweepy.API(oAuthHeader)
    try:
        myAPI.verify_credentials()
        validUser = True
    except:
        validUser = False
    
    if validUser == True:
        # Enact stream
        tweetStream = Stream(oAuthHeader, tweetStreamListener)
        tweetCount = 0
        tweetStreamStatus = 200
        eventHubStatus = 201
        streamDescriptionFull = ""
        while tweetCount < tweetLimit and tweetStreamStatus == 200 and eventHubStatus == 201:
            try:
                #general tweets
                #tweetStream.sample(async=False, languages=['en']) # Streams only english tweets.
                
                # Tweets with location
                # Filters tweets by english and tweets with locations only
                tweetStream.filter(languages=['en'], async=False, locations=[-180, -90, 180, 90]) 

                tweetCount = tweetStreamListener.num_tweets
                eventHubStatus = tweetStreamListener.hubStatusCode
                tweetStreamStatus = tweetStreamListener.twitterStatusCode
                streamDescriptionFull = tweetStreamListener.streamListenerMessage
            except:
                tweetCount = tweetStreamListener.num_tweets
                eventHubStatus = tweetStreamListener.hubStatusCode
                tweetStreamStatus = tweetStreamListener.twitterStatusCode
                streamDescriptionFull = tweetStreamListener.streamListenerMessage
                continue
    else:
        streamDescriptionFull = "Error validating Twitter API credentials. Please check your values again."

    return HttpResponse(streamDescriptionFull)

class EventHubClient(object):
    def __init__(self, eventHubName, namespace, policyName, sasKey):
        #super(TwitterStreamListenerFull, self).__init__()
        self.eventHubName = eventHubName
        self.namespace = namespace
        self.policyName = policyName
        self.sasKey = sasKey
    def sendMessage(self,body,partition):
        from azure.servicebus import ( _service_bus_error_handler )
        from azure.servicebus.servicebusservice import ( ServiceBusService, ServiceBusSASAuthentication)
        from azure.http import ( HTTPRequest, HTTPError)
        from azure.http.httpclient import _HTTPClient
        eventHubHost    = self.namespace + ".servicebus.windows.net"
        sasKeyName      = self.policyName
        sasKeyValue     = self.sasKey
        eventHubName    = self.eventHubName

        httpclient = _HTTPClient(service_instance=self)
        authentication = ServiceBusSASAuthentication(sasKeyName,sasKeyValue)
 
        request = HTTPRequest()
        request.method = "POST"
        request.host = eventHubHost
        request.protocol_override = "https"
        request.path = "/" + eventHubName + "/publishers/" + partition + "/messages?api-version=2014-05"
        request.body = body
        #request.headers.append(('Content-Type', 'application/json;charset=utf-8'))
        request.headers.append(('Content-Type', 'application/atom+xml;type=entry;charset=utf-8'))
 
        authentication.sign_request(request, httpclient)
 
        request.headers.append(('Content-Length', str(len(request.body))))
 
        status = 0
 
        try:
            resp = httpclient.perform_request(request)
            status = resp.status
        except Exception as ex:
            print "Failed to connect to the Event Hub. Code: "
            print str(ex)
            status = 404
        return status