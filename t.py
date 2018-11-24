import tweepy
import json
import csv
from textblob import TextBlob
from operator import itemgetter
import io

CONSUMER_KEY = "XXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXX"
ACCESS_KEY = "XXXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXXXXX"


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
searchterm = input("Enter the topic you want to search:")
max_tweets = int(input("Enter the number of tweets you want:"))
tweets = tweepy.Cursor(api.search, q=searchterm).items(max_tweets)
filename = input("Enter the filename:")
f = open(filename+'.txt', 'w')
f1 = open(filename+'.json', 'w')
writer = csv.writer(f)
writer.writerow(['Created At', 'ID', 'Text', 'Retweet Count',
                 'Friends Count', 'Favourites Count', 'Analysis'])
for i in tweets:
    f1.write(json.dumps(i._json))
#     analysis = TextBlob(i.text)
    print(i.text)
#     print("Sentiment:", analysis.sentiment)
    writer.writerow([str(i.created_at), str(i.id), str(i.text.encode('unicode_escape')), str(
        i.retweet_count), str(i.user.friends_count), str(i.user.favourites_count)])
f.close()
f1.close()
