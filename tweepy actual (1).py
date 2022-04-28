
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import tweepy as tw
import pandas as pd
import os
import datetime as DT
import numpy as np

consumer_key= 'FB45NdZElrRldR7hrbPyPfF22'
consumer_secret= 'ilFsqOzIiRJBUB0LB3iLcdqbFGkl0MMFz1uSP3gPQBqahPq47B'
access_token= '776150084430008321-FhDhfE3CTLJGlQRQpJOA0tophLU7n7w'
access_token_secret= '1YOb3anZG729a9pUieqeCPLYXcAERasKw5R9inW9TE8SU'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


listWords = ['best buy', 'walmart', 'lululemon', 'crocs', 'target', 'kohls', 'gamestop', 'dicks sporting goods', 'lowes', 'home depot', 'bed bath and beyond']
overallDict = []
for i in listWords: 
    search_words = i 
    today = DT.date.today()
    weekAgo = today - DT.timedelta(days=7)
    date_since = weekAgo
    
    tweets = tw.Cursor(api.search,
                      q=search_words,
                      lang="en",
                      since=date_since).items()
    tweets_info = [[tweet.text,tweet.created_at] for tweet in tweets]
    tweet_dataframe = pd.DataFrame(data=tweets_info,
                                  columns=['tweet',"date"])    
    overallDict[i] = [len(tweet_dataframe)]


print(overallDict)
output = pd.read_pickle("dfTweepy.pkl")

df = pd.DataFrame([overallDict], columns=list('ABCDEFGHIJK'))
newDataframe = output.append(df)
newDataframe.to_pickle("dfTweepy.pkl")