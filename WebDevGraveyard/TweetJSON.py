import json
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
body = str(json.dumps(tweetCookedJSON)).encode("ascii")