from twilio.rest import Client
import schedule
import random
import os
import time

#array with some cheesy good morning messages
good_morning_messages = [
    "Good Morning! Have a Great Day my Girl <3",
    "I love You Always", 
     "Good Morning Love, Hope You Slept well!"]



account_sid = 'your account sid here'
auth_token = 'your token here'
client = Client(account_sid, auth_token)

def send_message(quote):

 message = client.messages.create(
                            body=quote,
                            from_='whatsapp:+14155238886',
                            to='whatsapp:+353833012337')
  # print(message.sid)

#generates the random quote
quote = good_morning_messages[random.randint(0,len(good_morning_messages)-1)]
schedule.every().day.at("09:00").do(send_message,quote)

while True:

    schedule.run_pending()
    time.sleep(2)




