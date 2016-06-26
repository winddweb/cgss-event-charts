#! /usr/local/bin/python3

import csv
import sys
import os
import re
import plotly.plotly as py
import plotly.offline as pyof
import plotly.graph_objs as go

x_values = []
y_values_2 = []
y_values_10 = []
y_values_20 = []
y_values_60 = []
y_values_120 = []
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
                title, r_2k, r_10k, r_20k, r_60k, r_120k, _, link = t_text
            elif len(t_text) is 9:
                title, r_2k, r_10k, r_20k, r_60k, r_120k, _, date, link = t_text
            else:
                print(t_text)
                continue

            score_regex = r"：\d+（"

        if 'cindere_border' in sys.argv[1]:
            chart_type = "Predicted_Score"
            if len(t_text) is 8:
                title, date, r_2k, r_10k, r_20k, r_60k, r_120k, _ = t_text
            else:
                print(t_text)
                continue

            score_regex = r":\d+p"

        match_2 = re.search(score_regex, r_2k)
        match_10 = re.search(score_regex, r_10k)
        match_20 = re.search(score_regex, r_20k)
        match_60 = re.search(score_regex, r_60k)
        match_120 = re.search(score_regex, r_120k)

        x_values.append(t_date)
        append_matched(match_2, y_values_2)
        append_matched(match_10, y_values_10)
        append_matched(match_20, y_values_20)
        append_matched(match_60, y_values_60)
        append_matched(match_120, y_values_120)


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
    trace_60 = go.Scatter(
        x = x_values,
        y = y_values_60,
        name = "60000"
    )
    trace_120 = go.Scatter(
        x = x_values,
        y = y_values_120,
        name = "120000"
    )

    data = [trace_2, trace_10, trace_20, trace_60, trace_120]

    layout = dict(title = 'Event Score Trending @ CGSS ' + chart_type,
                  xaxis = dict(title = 'Date'),
                  yaxis = dict(title = 'Scores'),
                  showlegend=True,
                  legend = dict(
                    orientation= "h",
                    x=100,
                    y=1),
                  )

    fig = dict(data=data, layout=layout)

    # py.plot(fig, filename=chart_type + 'multiple-line') # save online on plot.ly, account required

    os.makedirs("html_charts/", exist_ok=True)

    pyof.plot(fig, filename='html_charts/' + chart_type + '_multiple-line.html')
