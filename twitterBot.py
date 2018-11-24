import tweepy
import textblob as TextBlob
from tweepy.auth import OAuthHandler
import time

# Secret User Data

CONSUMER_KEY = "XXXXXXXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXXXXXX"
ACCESS_KEY = "XXXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXXXXX"


# Authentication
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file = open("tweetInfo.txt", "a")


def updateStatus():
    msg = str(input("Tweet Message : "))
    api.update_status(msg)
    print("\nTweet Posted!\n")
    file.write("\nTweet Posted!!\n Message : " + msg + '\n')


def searchHash():
    search = str(input("Enter Search Query : #"))
    num = int(input("Number of Tweets to be Shown : "))
    tweets = tweepy.Cursor(api.search, q='#'+search).items(num)
    for i in tweets:
        file.write(i.text + "   By -->   " + i.user.name + '\n')


def searchUser():
    y = str(input("enter name: @"))
    u = api.get_user(y, include_entities=1)
    print("\nName: " + u.name + "\nDescription: " + u.description +
          "\nFollowers: " + str(u.followers_count) + "\nLocation: " + str(u.location) + "\nCreated: " + str(u.created_at) + "\n")
    # print(u)


user = api.me()

print("\n\nUsername : " + user.name + "\nFriends Count : " +
      str(user.friends_count) + "\nFollowers Count : " + str(user.followers_count) + "\nUser ID: " + str(user.id))
print("\n\n")

while True:
    print("Choose One : \n1.Post a Tweet.\n2.Search for HashTags.\n3.Get User Info.\n4.Exit\n")
    response = int(input())

    if response == 1:
        updateStatus()

    if response == 2:
        searchHash()

    if response == 3:
        searchUser()

    if response == 4:
        exit(0)

file.write("\n\n\n\n")
file.close()
