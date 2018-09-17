import feedparser
import time
import tweepy
import os
from bs4 import BeautifulSoup



consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()


feed_url = ('http://8bhomeworkassignments.blogspot.com/feeds/posts/default')

oldpublished = (public_tweets[0])
oldpublished = (oldpublished.text)

while True:

    feed = feedparser.parse(feed_url)
    
    #fixed, see commit desc
    newpublished = (feed['entries'][0]['title'])
    
    #also fixed, see commit desc
    if newpublished not in oldpublished:

        # Grabs the newest item from the feed with its title and content
        oldfeed = feedparser.parse(feed_url)
        title = (oldfeed['entries'][0]['title'])
        title = BeautifulSoup(title, "lxml").text
        content = (oldfeed['entries'][0]['content'][0]['value'])
        content = BeautifulSoup(content, "lxml").text

        oldpublished = (oldfeed['entries'][0]['published'])

        print (title)
        print (content)

        tweetthis = (title + '\n' + content)
        api.update_status(tweetthis)

    #also fixed, see commit desc
    elif newpublished in oldpublished:

        print ('Nothing new...')


    time.sleep(5)
