import os
import config
from twilio.rest import Client

account_sid = config.sid
auth_token = config.token_auth

client = Client(account_sid, auth_token)

def create_message(body: str, sender: str, reciever: str):

    message = client.messages \
                .create(
                     body = body,
                     from_= sender ,
                     to= reciever
                 )
    