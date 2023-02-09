from flask import Flask, request
from twilio.rest import Client
from keys import accounts_id, auth_token,twilio_number, my_phone_number
from regex_check import *

app=Flask(__name__)

@app.route('/send_message',methods=['POST'])
def send_message():
    try:
        phone_number = request.json['phone_number']
        message = request.json['message']
        check_reg = reg_check(phone_number, message)
        if check_reg:
            client = Client(accounts_id, auth_token)
            message = client.messages.create(
                             to=phone_number,
                             from_=twilio_number,
                             body=message)
            return 'Message sent successfully!'
        else:

            return 'check your details correctly'
    except:
        return 'Provide the details please'
if __name__ == '__main__':
    app.run()

