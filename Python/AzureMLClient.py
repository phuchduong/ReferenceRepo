class AzureMLClient:
	import urllib2
	import json


	def __init__(self):
		self.apiKey = ''
		self.postURL = ''
		self.columnNames = []
		self.requestBody = [ [],[] ]
		self.schemaBase = {
				"Inputs":{  
					"input1":{  
						"ColumnNames":[  
							# insert headers here, columnNames
						],
						"Values":[ 
						# insert answers here, requestBody
						# accepts an array of arrays
						]
					}
				},
				"GlobalParameters":{}
			}


	# executes a request to azure ml, if payload is valid
	def makePrediction(self):
		schemaReport = validSchema()
		if(schemaReport == 'valid'):
			prediction = sendResponse()
			return prediction
		else:
			return schemaReport


	# validates payload. Checks all the fields before building a
	# payload. Returns 'valid' if valid, and returns an error report
	# if not valid
	def validSchema():
		messageList = []
		if( len(self.apiKey) == 0 ):
			messageList.append("API key is missing.")
		elif( len(self.apiKey) != 88 ):
			# silently logs warning. Incase AzureML changes their API
			# keys in the future, this function won't break.
			print "Warning: the API key is not exactly 88 characters and may be invalid."
		
		if( len(self.postURL) == 0 ):
			messageList.append("Post URL for webservice is missing.")
		elif( len(self.apiKey) != 166 || len(self.apiKey) != 135 ):
			# silently logs warning. Incase AzureML changes their API
			# postURLs in the future, this function won't break.
			# newer post URLs have 166 characters. Legacy post URLs from beta
			# had 135 characters.
			print "Warning: the post URL is not exactly 166 or 135 characters and may be invalid."
		
		if( len(self.columnNames) == 0 ):
			messageList.append("Client requires column names.")
		
		try:
			if( type(self.requestBody[0]) != list):
				# if nested list array, it is a valid schema
				messageList.append("Client requires the request body to be a nested list of lists.")
				if( len(self.requestBody[0]) < 1):
					# checks if the first nested list is empty
					messageList.append("Empty inputs within the request body.")
		except Exception:
			# bad variable typing. Int, empty string, empty list etc.
			messageList.append("Client requires a valid request body.")
			pass

		if(if not messageList):
			messageReport = ' '.join(messageList)
			print messageReport # Logs error server side.
			return messageReport
		else:
			return 'valid'


	# Builds the request body from the base, column names and values
	# requestBody is a nested array: [ [],[],[] ]
	def buildSchema(self):
		schemaJSON = JSON.dumps(self.schemaBase)
		schemaJSON['Inputs']['input1']['ColumnNames'] = self.columnNames
		schemaJSON['Inputs']['input1']['Values'] = self.requestBody
		return schemaJSON

		
	# sends request to AzureML webservice, returns a response.
	def sendResponse(self):
		schemaJSON = buildSchema()
		schemaStr = str(schemaJSON)
		schemaEnc = str.encode(schemaStr)
		authorizationHeader = {'Content-Type':'application/json', 'Authorization':('Bearer '+ self.apiKey)}
		payload = urllib2.Request(self.postURL, schemaEnc, authorizationHeader) 
		response = urllib2.urlopen(payload)
		return response