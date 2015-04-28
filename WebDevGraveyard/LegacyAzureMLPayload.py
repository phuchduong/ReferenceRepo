#Get all objects from the model.
predictive_models_list = PredictiveModel.objects.all().order_by('experiment')

# Updates the CRF token
# CSRF token security check, for rendering templates.
c = {}
c.update(csrf(request))

#Gets the feature vector format, and parses the request into the feature vector parameters.
def getExperimentJSON(request, experimentName):
    import json
    # Obsolete 3/16/2015, old api payload.
    data =  {
       "Id": "score00001",
       "Instance": {
           "FeatureVector": {
                
           },
           "GlobalParameters": {
           }
       }
    }

	if experimentName=='titanic':
		# Obsolete 3/16/2015, old api payload.
		data['Instance']['FeatureVector'] = {
		   "AccommodationClass": request.POST.get('AccommodationClass'),
		   "Sex": request.POST.get('Sex'),
		   "Age": request.POST.get('Age'),
		   "SiblingSpouse": request.POST.get('SiblingSpouse'),
		   "ParentChild": request.POST.get('ParentChild'),
		   "Fare": request.POST.get('Fare'),
		   "Embarked": request.POST.get('Embarked'),
		}
	elif experimentName=='entityextractor':
        #Obsolete 3/16/2015, old api payload.
        data['Instance']['FeatureVector'] = {
           "inputText": request.POST.get('inputText'),
        }
    elif experimentName=='reviewrater':
        #Obsolete 3/16/2013, old api payload
        data['Instance']['FeatureVector'] = {
           "review": request.POST.get('inputText'),
        }