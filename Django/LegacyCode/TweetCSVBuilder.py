def on_data(self, data):
      # Converts the incoming payload to a JSON
      bodyJSON = json.loads(data)

      # Creates 
      bodyList = list()                                   #index
      bodyList.append("created_at,text,tweet_id,user_id,user_name,user_screen_name,user_location,geo,coordinates,place,language \n")
      bodyList.append(bodyJSON['created_at'])             #1
      tweetText = bodyJSON['text'].replace(",", "")
      bodyList.append(tweetText)                   #3
      bodyList.append(str(bodyJSON['id']))                #5
      bodyList.append(str(bodyJSON['user']['id']))        #7
      bodyList.append(bodyJSON['user']['name'])           #9
      bodyList.append(bodyJSON['user']['screen_name'])    #11
      bodyList.append(bodyJSON['user']['location'])       #13
      bodyList.append(str(bodyJSON['geo']))               #15
      bodyList.append(str(bodyJSON['coordinates']))       #17
      bodyList.append(str(bodyJSON['place']))             #19
      bodyList.append(bodyJSON['lang'])           #21
      bodyUni1 = "".join(bodyList)
      # Cleanses the string of all invalid characters
      bodyUni2 = unicodedata.normalize('NFKD', bodyUni1).encode('ascii','ignore')
      body = str(bodyUni2)

      # Cleanses the string of all invalid characters
      bodyUni2 = unicodedata.normalize('NFKD', bodyUni1).encode('ascii','ignore')
      body = str(bodyUni2)
      print body
      self.hubClient.sendMessage(body,str(bodyJSON['id']))