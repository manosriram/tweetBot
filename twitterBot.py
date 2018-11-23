import tweepy
import textblob as TextBlob
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import time
import jsonpickle

# Secret User Data
CONSUMER_KEY = "WKiSe8EKKU1Bx1C4Db9o5nslK"
CONSUMER_SECRET = "fOq5NXIwasrVzzTV9ioy3PILqgOjjhoBcm7bWtr6v6X86eRgSC"
ACCESS_KEY = "1065901711254908928-UY188v74sNXFtYbMLLiJ8DqJxvUKjv"
ACCESS_SECRET = "OrbFPaXDGqA6OvQytV3aKTdEVEQvbzOJWc6l2CtXHjJla"


# Authentication
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file = open("tweetInfo.txt", "a")


def updateStatus():
    msg = str(input("Tweet Message : "))
    api.update_status(msg)
    file.write("\nTweet Posted!!\n Message : " + msg + '\n')


def searchHash():
    search = str(input("Enter Search Query : #"))
    num = int(input("Number of Tweets to be Shown : "))
    tweets = tweepy.Cursor(api.search, q='#'+search).items(num)
    for i in tweets:
        file.write(i.text + "   By -->   " + i.user.name + '\n')


user = api.me()
name = user.name


print("Username : " + user.name + "\n Friends Count : " +
      str(user.friends_count) + "\nFollowers Count : " + str(user.followers_count) + "\nUser ID: " + str(user.id))

print("Choose One : \n1.Post a Tweet.\n2.Search for HashTags.3.Get User Info")


resp = str(input("Post a Tweet ??(yes/no) : "))
if resp == "yes":
    updateStatus()

resp1 = str(input("Search Hastags? (yes/no) : "))
if resp1 == "yes":
    searchHash()

y = str(input("enter name: @"))
y = "imVKohli"
u = api.get_user(y, include_entities=1)
print(u._json)
# print("\nName: " + u.name + "\nDescription: " + u.description +
#       "\nFollowers: " + str(u.followers_count) + "\n")

for t in u:
    print(t.status.text)

file.write("\n\n\n\n")
file.close()
