cgss-event-charts
===

Introduction
---
This Python script is developed for Cinderella Girls Starlight Stage players.(yeah, this is a game)
It will collect data from [@deresute_border](https://twitter.com/deresute_border) or [@cindere_border](https://twitter.com/cindere_border) who will keep updating current score borders and predictions for each tier.
Then it can generate event score trending charts based on the data.

Features
---

- Get Data from the Border Bot or the Predict Bot (twitter accounts) and save the data in a csv
- Draw line charts based on the csv files
- The line charts can be saved in one single local HTML file with interaction, or you can save it on plot.ly's server (free account required)
  - There are extra steps required for uploading to ploy.ly . Check the [instructions](https://plot.ly/python/getting-started/undefined)

How to use
---

1. Install the dependencies.
2. Config your plot.ly for hosting (optional if you only want to save the html locally)
3. Register Twitter Developer to get API tokens. [Here](https://apps.twitter.com) It's free and easy.
4. Change the config file `auth_settings_example.py`, rename it to `auth_settings.py` and fill in your token and secret.
4. Run Python scripts
```bash
# this one get the tweets and save it to a csv file

$ ./get_tweet_data.py [screen_name]
# screen_name is default to deresute_border, but you can also provide cindere_border to get the prediction data
# example output
$ ./get_tweet_data.py
200 tweets loaded
tweets from: 2016-05-02 07:35:02
400 tweets loaded
tweets from: 2016-04-26 08:33:04
600 tweets loaded
tweets from: 2016-04-24 06:33:03
800 tweets loaded
tweets from: 2016-04-22 04:33:02
1000 tweets loaded
584 of tweets recorded
# saved in deresute_border_tweets.csv

$ ./get_tweet_data.py cindere_border
tweets from: 2015-09-30 01:00:50
162 tweets loaded
8 of tweets recorded
# saved in cindere_border_tweets.csv
==========================

# this one draw the chart
$ ./draw_charts.py deresute_border_tweets.csv
# saved in html_charts/Current Scoremultiple-line
```

Screenshot
---
![screen shot 2016-05-04 at 3 12 38 am](https://cloud.githubusercontent.com/assets/1504159/15012085/aa303114-11aa-11e6-8967-0cf84fd83b4c.png)



Dependency
---

Python packages required
- [plotly](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjzoPPnmMDMAhUL5WMKHSVICcYQFggdMAA&url=https%3A%2F%2Fplot.ly%2F&usg=AFQjCNHB4w30_KQTWrrahRMIvlb0WRQXMQ&sig2=_xbfRs9kn8fUijYMBq0hNA) `pip3 install plotly`
- [tweepy]()
