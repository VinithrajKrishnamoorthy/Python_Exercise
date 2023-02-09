from twilio.rest import Client
from validation import *

account_sid = 'AC2703a1a3b897a667e486fbac4e764a0a'
auth_token = '4bcb39cd4244b9f744980c9fdcebbf5d'

twilio_number = '+16089753130'
try:
    mobile_number = input("Enter Phone Number:")
    message = input("Enter the Message to be Sent:")
    check_reg = reg_check(mobile_number, message)
    if check_reg:
        client = Client(account_sid,auth_token)
        message = client.messages.create(
                body = message,
                from_ = twilio_number,
                to = mobile_number,)
        print("Message Sent")
    else:
        print("Check your details Correctly")
except:
        print("Please provide Correct details")