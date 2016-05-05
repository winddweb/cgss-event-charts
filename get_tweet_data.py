#! /usr/local/bin/python3

import sys
import csv
from datetime import datetime
import tweepy
from auth_setting import auth_setting

# TODO: avoid twitter api rate limitation

def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(auth_setting["consumer_key"], auth_setting["consumer_secret"])
    auth.set_access_token(auth_setting["access_token"], auth_setting["access_token_secret"])

    api = tweepy.API(auth)

    # max_number = 400

    min_date = datetime(2016, 4, 29, 0, 00)
    max_date = datetime.today()

    # min_date = datetime(2016, 4, 20, 0, 00)
    # max_date = datetime(2016, 4, 29, 0, 00)

    # stream listener
    # class MyStreamListener(tweepy.StreamListener):

    #     def on_status(self, status):
    #         print(status.text)

    # myStreamListener = MyStreamListener()
    # myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    # myStream.filter(track=['デレステ'])

    # your own timeline
    # public_tweets = api.home_timeline()

    def stop_get_tweets(alltweets):
        stop = True

        # continue_get = len(alltweets) < max_number

        stop = alltweets[-1].created_at < min_date

        return stop

    alltweets = []

    # new_tweets = api.user_timeline(screen_name = screen_name, count=200)

    # alltweets.extend(new_tweets)

    # oldest = alltweets[-1].id - 1
    # oldest_date = alltweets[-1].created_at

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

    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]


    with open('%s_tweets.csv' % screen_name, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            # writer.writerow(["id","created_at","text"])
            writer.writerows(outtweets)

    pass

if __name__ == '__main__':
    #pass in the username of the account you want to download
    screen_name = sys.argv[1] if len(sys.argv) > 1 else "deresute_border"
    get_all_tweets(screen_name)

