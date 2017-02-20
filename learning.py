import tweepy
from tweepy import OAuthHandler
import json 

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Gives all your timeline satuses 
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text) 
 
def process_or_store(tweet):
    print(json.dumps(tweet))

#Gives all your timeline satuses as JSON
#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    process_or_store(status._json) 

#Gives all your followers
#for friend in tweepy.Cursor(api.friends).items():
#    process_or_store(friend._json)

#Gives all your tweets
#for tweet in tweepy.Cursor(api.user_timeline).items():
#    process_or_store(tweet._json)


