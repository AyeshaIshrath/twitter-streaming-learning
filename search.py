from slistener import SListener
import time, tweepy, sys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class listener(StreamListener):

    def on_data(self, data):
        print data
        return True


twitterStream = Stream(auth, listener())

string = raw_input("Enter the string to be searched\n")
tweets_data_path = '/home/ayesha/test.json'
tweets_file = open(tweets_data_path, "a")
tweets_file.write(twitterStream.filter(track = ['string'])) 
