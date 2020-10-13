import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'jLhZznt5z0SjIBVfCHpqJxqgb'
consumer_secret = 'OMVLGqBRLRTsPzTQRGLHBSNQs4RIUznxpxxphvBH3JOtNb51cc'
access_token = '1239077146087157760-dPjfZCyFrDUi0aJaPnyoXxC7LZNEwk'
access_token_secret = 'GbzTFLXOhX37MjQMGC3YxV6gr4Gk5JdZnNXOLuCosFDRK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#justiceforSSR",count=10,
                           lang="en",
                           since="2020-08-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])