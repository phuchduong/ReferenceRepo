def on_data(self, data):
      # Converts the incoming payload to a JSON
      bodyJSON = json.loads(data)

      # Creates 
      bodyList = list()                                   #index
      bodyList.append("{\"created_at\":\"")               #0
      bodyList.append(bodyJSON['created_at'])             #1
      bodyList.append("\",\"text\":\"")                   #2
      bodyList.append(bodyJSON['text'])                   #3
      bodyList.append("\",\"tweet_id\":\"")               #4
      bodyList.append(str(bodyJSON['id']))                #5
      bodyList.append("\",\"user_id\":\"")                #6
      bodyList.append(str(bodyJSON['user']['id']))        #7
      bodyList.append("\",\"user_name\":\"")              #8
      bodyList.append(bodyJSON['user']['name'])           #9
      bodyList.append("\",\"user_screen_name\":\"")       #10
      bodyList.append(bodyJSON['user']['screen_name'])    #11
      bodyList.append("\",\"user_location\":\"")          #12
      bodyList.append(bodyJSON['user']['location'])       #13
      bodyList.append("\",\"geo\":\"")                    #14
      bodyList.append(str(bodyJSON['geo']))               #15
      bodyList.append("\",\"coordinates\":\"")            #16
      bodyList.append(str(bodyJSON['coordinates']))       #17
      bodyList.append("\",\"place\":\"")                  #18
      bodyList.append(str(bodyJSON['place']))             #19
      bodyList.append("\",\"language\":\"")               #20
      bodyList.append(bodyJSON['lang'])                   #21
      bodyList.append("\"}")                              #22
      bodyUni1 = "".join(bodyList)

      # Cleanses the string of all invalid characters
      bodyUni2 = unicodedata.normalize('NFKD', bodyUni1).encode('ascii','ignore')
      body = str(bodyUni2)
      print body
      self.hubClient.sendMessage(body,str(bodyJSON['id']))