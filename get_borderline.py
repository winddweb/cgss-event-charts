#! /usr/local/bin/python3

import sys
import sh


option = sys.argv[1] # predict or border

get_tweet = sh.Command('./get_tweet_data.py')

draw_chart = sh.Command('./draw_charts.py')

if option == 'border':
    # ./get_tweet_data.py deresute_border
    # ./draw_charts.py deresute_border_tweets.csv
    output = get_tweet('deresute_border')
    print(output)
    draw_chart('deresute_border_tweets.csv')
elif option == 'predict':
    # ./get_tweet_data.py cindere_border
    # ./draw_charts.py cindere_border_tweets.csv
    output = get_tweet('cindere_border')
    print(output)
    draw_chart('cindere_border_tweets.csv')
else:
    print('Please give "predict" or "border" as the first argument')