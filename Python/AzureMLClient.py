class AzureMLClient:
	import urllib2
	import json

	def __init__(self):
		self.apiKey = ''
		self.postURL = ''
		self.columnNames = []
		self.requestBody = []
		self.schemaBase = {  
		   "Inputs":{  
		      "input1":{  
		         "ColumnNames":[  
		            # insert headers here, columnNames
		         ],
		         "Values":[ #insert answers here, requestBody
		         ]
		      }
		   },
		   "GlobalParameters":{}
		}

	def makePrediction(self):
		if(validSchema == 'valid'):
		else:
			return ''
			

	def validSchema():
		messageList = []
		if(if not self.apiKey):
			messageList.append("API key is missing.")
		elif(if not self.postURL):
			messageList.append("Post URL for webservice is missing.")
		elif(if not self.columnNames):
			messageList.append("Client requires column names.")
		elif(if not self.requestBody):
			messageList.append("Client requires request body.")

		if(if not messageList):
			messageReport = ''.join(messageList)
			print messageReport
			return 'invalid'
		else
			return 'valid'

	# Builds the request body from the base, column names and values
    def buildSchema(self):
    	schemaJSON = JSON.dumps(self.schemaBase)
    	schemaJSON['Inputs']['input1']['ColumnNames'] = self.columnNames
    	schemaJSON['Inputs']['input1']['Values'] = self.requestBody
    	return schemaJSON

	def sendResponse(self):
		schemaJSON = buildSchema()
		schemaStr = str(schemaJSON)
    	schemaEnc = str.encode(schemaStr)
		authorizationHeader = {'Content-Type':'application/json', 'Authorization':('Bearer '+ self.apiKey)}
	    payload = urllib2.Request(self.postURL, schemaEnc, authorizationHeader) 
	    response = urllib2.urlopen(payload)
	    return response