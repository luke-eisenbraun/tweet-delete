import tweepy
import config
from datetime import datetime, timedelta

# options
test_mode = config.test_mode
verbose = config.verbose
delete_tweets = config.delete_tweets
delete_favs = config.delete_favs
days_to_keep = config.days_to_keep

tweets_to_save = config.tweets_to_save
favs_to_save = config.favs_to_save

# auth and api
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# set cutoff date, use utc to match twitter
cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)

# delete old tweets
if delete_tweets:
    # get all timeline tweets
    print("Retrieving timeline tweets")
    timeline = api.user_timeline()
    deletion_count = 0
    ignored_count = 0

    for tweet in timeline:
        # where tweets are not in save list and older than cutoff date
        if tweet.id not in tweets_to_save and tweet.created_at < cutoff_date:
            if verbose:
                print("Deleting %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text))
            if not test_mode:
                api.destroy_status(tweet.id)

            deletion_count += 1
        else:
            ignored_count += 1

    print("Deleted %d tweets, ignored %d" % (deletion_count, ignored_count))
else:
    print("Not deleting tweets")

# unfavor old favorites
if delete_favs:
    # get all favorites
    print("Retrieving favorite tweets")
    favorites = tweepy.Cursor(api.favorites).items()
    unfav_count = 0
    kept_count = 0

    for tweet in favorites:
        # where tweets are not in save list and older than cutoff date
        if tweet.id not in favs_to_save and tweet.created_at < cutoff_date:
            if verbose:
                print("Unfavoring %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text))
            if not test_mode:
                api.destroy_favorite(tweet.id)

            unfav_count += 1
        else:
            kept_count += 1

    print("Unfavored %d tweets, ignored %d" % (unfav_count, kept_count))
else:
    print("Not unfavoring tweets")
