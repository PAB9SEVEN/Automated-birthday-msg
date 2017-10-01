import time
import calendar
import datetime
import twilio
from twilio.rest import TwilioRestClient
print "Year"
eventime='02:20:00'
year=raw_input("-->")

print "Month"
month=raw_input("-->")

print "Day"
day=raw_input("-->")

eventdate=day+'/'+month+'/'+year
print eventdate
todaydate=time.strftime('%d/%m/%y')
print todaydate
today=time.strftime('%I:%M:%S')
print today
while(eventdate!=todaydate):
    todaydate=time.strftime('%d/%m/%y')
    #print todaydate
#print todaydate
if(eventdate==todaydate):    
    while(today!=eventime):
        today=time.strftime('%I:%M:%S')
        print today
    if(today==eventime):
        print "yead"
        # Your Account SID from twilio.com/console
        account_sid = "ACea0dca81b18bd10b2192c8aee809445e"
        # Your Auth Token from twilio.com/console
        auth_token  = "56945ad8e052ae5dd96cff577357f6d7"

        client = TwilioRestClient(account_sid, auth_token)

        message = client.messages.create(
            to="+917030886289", 
            from_="+12319946006 ",
            body="Happy Birthday <3 :*")

        print(message.sid)
        print("message sent successfully")
              
