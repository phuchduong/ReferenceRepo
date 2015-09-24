#json1
if isinstance(jsonStr, unicode):
   body = jsonStr.encode("utf-8")
else:
   jsonStr.decode("utf-8") # optional check whether it is correct UTF-8
   body = jsonStr

#json2
body = json.dumps(data).encode("ascii")

#json3
body = json.dumps(data).encode('utf8')

#json4 WORKS
body = str(data)

#json5 WORKS
body = str(data).encode("ascii")

#json6
body = str(data).encode("utf8")

#May 4
#json2
tweetRawJSON = json.loads(data)
tweetCookedJSON = {}
tweetCookedJSON['created_at'] = tweetRawJSON['created_at']
tweetCookedJSON['text'] = tweetRawJSON['text']
	#serialization error
body = str(tweetCookedJSON).encode("ascii")

#json3
tweetRawJSON = json.loads(data)
tweetCookedJSON = {}
tweetCookedJSON['created_at'] = tweetRawJSON['created_at']
tweetCookedJSON['text'] = tweetRawJSON['text']

body = str(json.dumps(tweetCookedJSON)).encode("ascii")