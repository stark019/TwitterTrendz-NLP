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
csvFile = open('tweets.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)
c=0
hashtag = str(input("enter the hashtag you want to search for : "))
date = str(input("since YYYY-MM-DD :"))
for tweet in tweepy.Cursor(api.search,q=hashtag,count=100,
                           lang="en",
                           since=date).items():
    if(c<100):
        c+=1
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    else:
        break

csv_file = 'tweets.csv'
txt_file = 'tweettext.txt'
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()