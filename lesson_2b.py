# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: Python_Foundations
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: lesson_2b
 * Date: 10/2/15
 * Time: 10:06 PM
 * To change this template use File | Settings | File Templates.
"""
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACf3b3c38f0267279c69d4005aead597d0"
auth_token = "b36cee7b078e029b5fe338c257b48969"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Iraquitan?",
                                 to="+5591982894092",    # Replace with your phone number
                                 from_="+14233908077")  # Replace with your Twilio number
print message.sid
