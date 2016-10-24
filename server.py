#!/usr/bin/python

from flask import Flask, request, redirect
from espeak import espeak
import twilio.twiml
import urllib, pycurl, os

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
        """Respond to incoming calls with a simple text message."""
        sms = request.args.get('Body')
        resp = twilio.twiml.Response()
        #resp.message("Hello, Mobile Monkey")
        return str(resp)

if __name__ == "__main__":
	print ("Hello twilio")
app.run( host='0.0.0.0', debug=True, port = 80)

espeak.synth(resp)
