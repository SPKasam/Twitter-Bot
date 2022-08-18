import tweepy
import time
from tweepy.auth import OAuth2BearerHandler

auth = tweepy.OAuth1UserHandler(
   "XuHG0bcwCX0GH9qfm15Tt4qXM", "fKfRYiv3VVbPwCNHgVrH5iIpNWfmvqhRdP7x5tekYqZpg2covp",
   "3277926859-4uTmYfh4EvQGH91nQcQYGepMTWaHBs9qYA58loD", "cytqdUhur05mfLIcRSsc3O4CITVi1NItW0Tk6mLWGUR9i"
)
api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.TooManyRequests:
        time.sleep(1)

search_string = 'giveaway'
numOfTweets = 2

# for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
#     try:
#         if follower.followers_count > 100000:
#             print(follower.name)
#     except StopIteration:
#         break

for tweet in tweepy.Cursor(api.search_tweets,search_string).items(numOfTweets):
    try:
        print(f'User: {tweet.user.screen_name}')
        print(f'Post: {tweet.text}\n')
        # api.retweet(tweet.id)
        # api.like(tweet.id)
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break
