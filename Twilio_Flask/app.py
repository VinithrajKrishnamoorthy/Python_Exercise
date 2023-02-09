from flask import Flask
from flask import request
from twilio.rest import Client

app = Flask(__name__)
@app.route('/sms',methods = ['POST'])

def sms():
    if request.method == "POST":
        mobile_number = request.form["mobile_number"]
        message = request.form["message"]
        
        account_sid = 'AC2703a1a3b897a667e486fbac4e764a0a'
        auth_token = '4bcb39cd4244b9f744980c9fdcebbf5d'

        twilio_number = '+16089753130'
        mobile_number = '+919994408342'

        client = Client(account_sid,auth_token)
        message = client.messages.create(
                body = message,
                from_ = twilio_number,
                to = mobile_number,)
        return "Message Send"
if __name__ == '_main_':
    app.run()