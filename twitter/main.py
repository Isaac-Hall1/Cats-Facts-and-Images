import requests
import os
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

class CatFactaas:
    def __init__(self):
      self.imgUrl = None
      self.fact = None
      self.status = None

  
  # sets the image for cat 
    def getCatImage(self) -> None:
      urlcat = "https://cataas.com/cat?json=true"
      r = requests.get(urlcat, params={"json": "true"})
      data = r.json()
      self.imgUrl = "https://cataas.com" + data['url']


# sets self.fact to the cat facts :3
    def getCatFact(self) -> None:
      url = "https://cat-fact.herokuapp.com/facts/random"
      r = requests.get(url)
      data = r.json() 
      
      while not data['status']['verified']:
        # None
        r = requests.get(url)
        data = r.json()
        self.fact = data['text']
        if data['status']['verified']:
          break

    def sendText(self, destination: str) -> None:
      account_sid = os.environ['TWILIO_ACCOUNT_SID']
      auth_token = os.environ['TWILIO_AUTH_TOKEN']
      client = Client(account_sid, auth_token)
      message = client.messages.create(media_url=self.imgUrl, body = self.fact, from_='+19402908870', to=destination)
      self.status = message.sid



if __name__ == "__main__":
  c = CatFactaas()
  c.getCatImage()
  c.getCatFact()
  c.sendText(destination= os.environ['PHONENUMBER'])







#https://www.twilio.com/docs/sms/quickstart/python