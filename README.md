cgss-event-charts
===

Introduction
---
This Python script is developed for Cinderella Girls Starlight Stage players.(yeah, this is a game)
If you don't know what CGSS is probably you should not be here. Just in case you want to know what it is, check this [reddit](https://www.reddit.com/r/StarlightStage/comments/4h3eg7/event_megathread_live_groove_dance_burst_seizon/)

What it does is that it will collect data from [@deresute_border](https://twitter.com/deresute_border) or [@cindere_border](https://twitter.com/cindere_border) who will keep updating current score borders and predictions for each tier.
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
5. Run Python scripts

One liner:
---

`$ ./get_borderline.py [predict/border]`

**Example**

```bash
$ ./get_borderline.py border
200 tweets loaded
tweets from: 2016-05-03 10:48:03
400 tweets loaded
tweets from: 2016-05-01 08:47:02
600 tweets loaded
466 of tweets recorded

$ ./get_borderline.py predict
163 tweets loaded
4 of tweets recorded
```

**Run `get tweet data` and `draw charts` separately**

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

Live Demo
---

https://winddweb.github.io/cgss-event-charts/

Dependency
---

Python packages required

- [plotly](https://plot.ly) `pip3 install plotly`
- [tweepy](http://docs.tweepy.org/en/v3.5.0/) `pip3 install tweepy`
- [sh](http://amoffat.github.io/sh/) ``pip3 install sh``
