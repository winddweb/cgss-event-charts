#! /usr/local/bin/python3

import csv
import sys
import re
import plotly.plotly as py
import plotly.offline as pyof
import plotly.graph_objs as go

x_values = []
y_values_2 = []
y_values_10 = []
y_values_20 = []
y_values_50 = []
y_values_100 = []
chart_type = ""

def append_matched(match, y_list):
    if match:
        score = match.group().replace('：','').replace('（', '').replace(':', '').replace('p', '')

        y_list.append(score)

with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        t_id, t_date, t_text = row

        t_text = t_text.split('\n')

        if 'deresute_border' in sys.argv[1]:
            chart_type = "Current_Score"
            if '最終結果' in t_text[0]:
                title, r_2k, r_10k, r_20k, r_50k, r_100k, _, link = t_text
            else:
                title, r_2k, r_10k, r_20k, r_50k, r_100k, _, date, link = t_text

            score_regex = r"：\d+（"

        if 'cindere_border' in sys.argv[1]:
            chart_type = "Predicted_Score"
            title, date, r_2k, r_10k, r_20k, r_50k, r_100k, _ = t_text
            score_regex = r":\d+p"

        match_2 = re.search(score_regex, r_2k)
        match_10 = re.search(score_regex, r_10k)
        match_20 = re.search(score_regex, r_20k)
        match_50 = re.search(score_regex, r_50k)
        match_100 = re.search(score_regex, r_100k)

        x_values.append(t_date)
        append_matched(match_2, y_values_2)
        append_matched(match_10, y_values_10)
        append_matched(match_20, y_values_20)
        append_matched(match_50, y_values_50)
        append_matched(match_100, y_values_100)


    trace_2 = go.Scatter(
        x = x_values,
        y = y_values_2,
        name = "2000"
    )

    trace_10 = go.Scatter(
        x = x_values,
        y = y_values_10,
        name = "10000"
    )
    trace_20 = go.Scatter(
        x = x_values,
        y = y_values_20,
        name = "20000"
    )
    trace_50 = go.Scatter(
        x = x_values,
        y = y_values_50,
        name = "50000"
    )
    trace_100 = go.Scatter(
        x = x_values,
        y = y_values_100,
        name = "100000"
    )

    data = [trace_2, trace_10, trace_20, trace_50, trace_100]

    layout = dict(title = 'Event Score Trending @ CGSS ' + chart_type,
                  xaxis = dict(title = 'Date'),
                  yaxis = dict(title = 'Scores'),
                  )

    fig = dict(data=data, layout=layout)

    # py.plot(fig, filename=chart_type + 'multiple-line') # save online on plot.ly, account required
    pyof.plot(fig, filename='html_charts/' + chart_type + '_multiple-line.html')
