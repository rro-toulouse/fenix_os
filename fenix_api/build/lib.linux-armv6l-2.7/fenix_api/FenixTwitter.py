#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
import time

class FenixTwitter:
    
    def __init__(self): # Constructor
        self.Main()

    def Main(self):
        consumer_key = 'jaL8cPgN86MiXI0tCLYEzC1xc'
        consumer_secret = 'okaIFI0m3dayTAk2w2qvjWJYjkNFkXxXzVzU9H9Pfmo47K5PZw'
        access_token_key = '4177870763-fOib4cgEjTbenGGAI4i3UeziszPiaUIrnSsiN4v'
        access_token_secret = 'h185EIXJY37Ex7LM5OR9dsrS9XLSV8ehrgRHZb67M5Hpp'
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    
    def Request(self):
        r = self.api.request('statuses/home_timeline', {'count':1})
        return r

    def GetTweets(self):
        r = ''
        try:
            r = self.api.request('search/tweets', {'q':'@epitechtoulouse', 'count':'100'})
        except Exception as e:
           time.sleep(1)
           print("failed")
           self.GetTweets()
        tweets = []
        for item in r:
            item['text'].encode("utf-8", errors='ignore')
            if item['text'][0:2] != 'RT':
                tweets.append(item['text'])
        return tweets
        
