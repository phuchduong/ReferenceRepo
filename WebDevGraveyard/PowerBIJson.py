if self.powerBI == 1:
    # Power BI currently can't handle the full payload of a tweet
    # Json, so this if statement is necessary to scale down the JSON
    # to bare bones information. This slows down the server compared to
    # just dumping the full JSON into the event hub.
    tweetRawJSON = json.loads(data)
    tweetCookedJSON = {}
    tweetCookedJSON['created_at'] = tweetRawJSON['created_at']
    tweetCookedJSON['text'] = tweetRawJSON['text']
    tweetCookedJSON['tweet_id'] = tweetRawJSON['id']
    tweetCookedJSON['user_id'] = tweetRawJSON['user']['id']
    tweetCookedJSON['user_name'] = tweetRawJSON['user']['name']
    tweetCookedJSON['user_screen_name'] = tweetRawJSON['user']['screen_name']
    tweetCookedJSON['user_location'] = tweetRawJSON['user']['location']
    tweetCookedJSON['geo'] = tweetRawJSON['geo']
    tweetCookedJSON['coordinates'] = tweetRawJSON['coordinates']
    tweetCookedJSON['place'] = tweetRawJSON['place']
    tweetCookedJSON['tweet_number'] = self.num_tweets

    #encodes it into python 2.XX as ascii [str(data).encode("utf-8") which is the 
    #equivalent to .NET UTF-8. if python 3.XX then str(data).encode("utf-8"). 
    #If C# then GetBytes(Data)
    body = str(json.dumps(tweetCookedJSON)).encode("ascii")
else:
    # This is the prefered method to push tweets. It's faster than the powerBI
    # scaling down. It gives more information also. It's also easier on the server.
    # Please only use the powerBI setting if powerBI is actually used.
    body = str(data)

# sends partition and tweet body to azure event hub.
self.hubStatusCode = self.hubClient.sendMessage(body,partion)