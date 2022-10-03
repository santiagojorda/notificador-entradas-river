import tweepy
from src.credentials import API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET, BEARER_TOKEN


# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id=API_KEY 
#     redirect_uri="Callback / Redirect URI / URL here",
#     scope=["Scope here", "Scope here"],
#     # Client Secret is only necessary if using a confidential client
#     client_secret="Client Secret here"
# )
# client = tweepy.Client(BEARER_TOKEN)
# api = tweepy.API(auth)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweet(msg):
    print(msg)
    api.update_status(msg)