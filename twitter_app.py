# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:50:55 2017

@author: Satheesh
"""

import tweepy
import csv

from textblob import TextBlob

consumer_key =	'howuDVCDR8f63eYCnSIrm4kX2'
consumer_secret = 'DvfottTuO81adluMbt3SBNV2pgAZLKhLJmbBPxoARQfOmHpgz9'

access_token = '2874878936-1t1dgKcJPXZ65pVxsStL1zFLDqY63F92d0e4Cbx'
access_token_secret = '2A6OUFB52ic7D6eGRB4Um8lqo4n7kmzz4YNuUmXRkf1Dl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('machine')

#Github challenge siraj.. save tweets in csv file
with open('tweets.csv','w', encoding = 'utf-8') as fp:
    writer = csv.writer(fp)
    for tweet in public_tweets:
        text = tweet.text
        tweet = TextBlob(tweet.text)
        if tweet.sentiment.polarity < 0:
            score = 'positive'
        else:
            score = 'negative'
        writer.writerow([text, score])    