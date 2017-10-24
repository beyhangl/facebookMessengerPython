# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render



from django.views import generic

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,requests, random, re
from pprint import pprint
from django.utils.decorators import method_decorator
import sqltest as sqlop
from fbmq import Page
import fbmq
from fbmq import Attachment, Template, QuickReply, Page
def post_facebook_message(fbid, recevied_message):           

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=XXXXX' 

    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())



# Create your views here.
class YoMamaBotView(generic.View):
    page = fbmq.Page('XXX')
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'XXX':
            print('verify is ok')
            return HttpResponse(self.request.GET['hub.challenge'])

        else:

            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):

        # Converts the text payload into a python dictionary

        incoming_message = json.loads(self.request.body.decode('utf-8'))
        #print(str(incoming_message)+ ' +++++')
        # Facebook recommends going through every entry since they might send

        # multiple messages in a single call during high load
        #page = fbmq.Page('EAAXTQIyKBiwBAMnl26FWLW7T6ZBCsD3TFPRcRxIaYU4YkMjrKosWZBwXDyLZBRzWfIXZCvWLLZCGF8bqixLDKXm8mFA7SNSbJjTfnagkDmeZBLM6ZA9yTDD5RRjTbcoRQWexH0qcnNM8ZAsFrUs3oQxgbtAJYlHaFZCS88cr1d90pawZDZD')
        #page.send('1488848524485107', "hello world!")

 
        for entry in incoming_message['entry']:
            for message in entry['messaging']:

                # Check to make sure the received call is a message call

                # This might be delivery, optin, postback for other events 

                if 'message' in message:

                    # Print the message to the terminal
                    #print(message['message']+ ' ++++ message text')  
                    try:
                     #post_facebook_message(message['sender']['id'], message['message']['text'])
                     sqlop.letsinsert(str(message['sender']['id']),str(message['message']['text']),str(message['message']['seq']))
                     pprint(message)
                     pprint(message['recipient']['id'])
                    except:
                     pprint('Kayit olmadi')
                     post_facebook_message(message['sender']['id'],'Üzgünüm sizi anlayamadım')
        return HttpResponse()

