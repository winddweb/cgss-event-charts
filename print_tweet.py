#! /usr/local/bin/python3

import sys
from datetime import datetime, timedelta
import tweepy
from auth_setting import auth_setting

# TODO: avoid twitter api rate limitation

def get_all_tweets(screen_name, max_number):

    auth = tweepy.OAuthHandler(auth_setting["consumer_key"], auth_setting["consumer_secret"])
    auth.set_access_token(auth_setting["access_token"], auth_setting["access_token_secret"])

    api = tweepy.API(auth)

    # max_number = 400

    min_date = datetime(2016, 6, 20, 0, 00)
    max_date = datetime.today() + timedelta(days=1) # to fix timezone

    def stop_get_tweets(alltweets):
        stop = True

        # continue_get = len(alltweets) < max_number

        stop = alltweets[-1].created_at < min_date

        if max_number is not None:
            stop = stop or len(alltweets) < max_number

        return stop

    def filter_tweets(alltweets):

        # filtered =

        # return filtered

        pass

    alltweets = []

    oldest = None

    while True:
        if oldest is None:
            new_tweets = api.user_timeline(screen_name = screen_name, count=200)
        else:
            new_tweets = api.user_timeline(screen_name = screen_name, count=200,max_id=oldest)

            print("tweets from: %s" % oldest_date)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        oldest_date = alltweets[-1].created_at

        print("%s tweets loaded" % len(alltweets))

        if stop_get_tweets(alltweets):

            alltweets = [tweet for tweet in alltweets if min_date < tweet.created_at < max_date]
            print("%s of tweets recorded" % len(alltweets))
            break

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

    print(outtweets)

    pass

if __name__ == '__main__':
    #pass in the username of the account you want to download
    screen_name = sys.argv[1] if len(sys.argv) > 1 else "cindere_border"
    max_number = sys.argv[2] if len(sys.argv) > 2 else None

    get_all_tweets(screen_name, max_number)

