import tweepy
from src.credentials import API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet(msg):
    print(msg)
    api.update_status(msg)