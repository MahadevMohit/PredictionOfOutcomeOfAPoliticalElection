from fileinput import filename
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
tweets = []

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):


    def on_data(self, data):
       
        tweet = json.loads(data)

        if 'text' in tweet:
            createdAt = tweet['created_at']
            tweetId =  tweet['id']
            userId = tweet['user']['id']
            userName = tweet['user']['name']
            tweetText = tweet['text']

        else:
            createdAt = " "
            tweetId = " "
            userId = " "
            userName = " "
            tweetText = " "

        with open('tweets.csv', 'a') as f:

            from csv import writer
            csv = writer(f)
            row = [createdAt,tweetId,userId,userName,tweetText]
            values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
            csv.writerow(values)

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
stream.userstream(track='@realDonalTrump') 

