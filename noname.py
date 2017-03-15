# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:20:35 2017

@author: Satheesh
"""

from textblob import TextBlob

wiki = TextBlob("satheesh will be great one day")

print(wiki.tags)
#bag of words representation
print(wiki.words)
#sentiment score
print(wiki.sentiment.polarity)