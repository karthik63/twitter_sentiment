import json
from twython import Twython
import pymongo
import dateutil.parser
import datetime
from pymongo import MongoClient
import numpy as np
import pytz
import nltk
import re
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import matplotlib.pyplot as plt
import matplotlib.dates
import matplotlib
import word_lookup
from mpl_toolkits.basemap import Basemap

def senti_tweet(db_name, collection_name, ne):

    connection = MongoClient()

    db = connection[db_name]

    number = 0

    sentiscore = 0

    records = db[collection_name].find({"ne_list" : ne})

    for record in records:

        number += 1

        sentiscore += record["sentiment"]["compound"]

    return number, sentiscore / number

def senti_news(db_name, collection_name):

    connection = MongoClient()

    db = connection[db_name]

    number = 0

    sentiscore = 0

    records = db[collection_name].find()

    for record in records:

        number += 1

        sentiscore += record["sentiment"]["compound"]

    return number, sentiscore / number

def histogram1():
    x = ["easter", "jesus", "trump", "bts", "india"]
    y = [0.517, 0.488, 0.0826, 0.833, -0.056]

    plt.xlabel("Named Entities")
    plt.ylabel("Average sentiment")

    plt.bar(range(len(y)), y, align='center')
    plt.xticks(range(len(x)), x, size='small')
    plt.show()

def histogram2():
    fig, ax = plt.subplots()

    x = ["easter", "jesus", "trump", "bts", "india"]
    y = [0.469, 0.1853, -0.1486, 0.1815, 0.114]

    ind = np.arange(5)  # the x locations for the groups
    width = 0.35  # the width of the bars
    p1 = ax.bar(ind, y, width, color='g')

    y = [0.517, 0.488, 0.0826, 0.833, -0.056]

    p2 = ax.bar(ind + width, y, width,
                color='orange')

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(x)

    plt.xlabel("Named Entities")
    plt.ylabel("Average sentiment")

    ax.legend((p1[0], p2[0]), ('Tweets', 'News'))
    plt.show()


def line_graph1_news(db_name, collection_name):

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    records = collection.find()

    dates = []

    sentiment = []

    for record in records:

        dates.append(record["datetime_format"])

        sentiment.append(record["sentiment"]["compound"])

    dates = np.array(dates)

    sentiment = np.array(sentiment)

    indices = np.argsort(dates)

    dates = dates[indices]

    sentiment = sentiment[indices]

    plt.figure(figsize=(30, 4))

    dates = matplotlib.dates.date2num(dates)
    plt.plot_date(dates, sentiment, linestyle="solid", marker=",")

    plt.xlabel("Time")
    plt.ylabel("Sentiment")

    plt.show()

def line_graph1_tweet(db_name, collection_name, ne):

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    records = collection.find({"ne_list": ne})

    dates = []

    sentiment = []

    for record in records:

        dates.append(record["datetime_format"])

        sentiment.append(record["sentiment"]["compound"])

    dates = np.array(dates)

    sentiment = np.array(sentiment)

    indices = np.argsort(dates)

    dates = dates[indices]

    sentiment = sentiment[indices]

    plt.figure(figsize=(30, 4))

    dates = matplotlib.dates.date2num(dates)
    plt.plot_date(dates, sentiment, linestyle="solid", marker=",")

    plt.xlabel("Time")
    plt.ylabel("Sentiment")

    plt.show()

def line_graph2(db_name, collection_name, ne):

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    records = collection.find({"ne_list": ne})

    dates = []

    sentiment = []

    for record in records:

        dates.append(record["datetime_format"])

        sentiment.append(record["sentiment"]["compound"])

    dates = np.array(dates)

    sentiment = np.array(sentiment)

    indices = np.argsort(dates)

    dates = dates[indices]

    sentiment = sentiment[indices]

    plt.figure(figsize=(30, 4))

    dates = matplotlib.dates.date2num(dates)
    plt.plot_date(dates, sentiment, linestyle="solid", marker=",")

    #######################################################################

    db = connection[db_name]

    collection = db[ne]

    records = collection.find()

    dates = []

    sentiment = []

    for record in records:
        dates.append(record["datetime_format"])

        sentiment.append(record["sentiment"]["compound"])

    dates = np.array(dates)

    sentiment = np.array(sentiment)

    indices = np.argsort(dates)

    dates = dates[indices]

    sentiment = sentiment[indices]

    dates = matplotlib.dates.date2num(dates)
    plt.plot_date(dates, sentiment, color="b", linestyle="solid", marker=",")

    plt.show()

def spatial_tweet(db_name, collection_name, ne):
    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    records = collection.find({"ne_list": ne})

    m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='i')

    #m.drawcoastlines()
    m.fillcontinents(color='yellow', lake_color='aqua')
    # draw parallels and meridians.
    #m.drawparallels(np.arange(-90., 91., 30.))
    #m.drawmeridians(np.arange(-180., 181., 60.))
    m.drawmapboundary(fill_color='aqua')


    plt.legend()

    latitudes_pos = []

    latitudes_neg = []

    longitudes_pos = []

    longitudes_neg = []

    for record in records:

        if not "location_latitude" in record:
            continue


        if record["sentiment"]["compound"] >= 0:
            latitudes_pos.append(record["location_latitude"])

            longitudes_pos.append(record["location_longitude"])

        else:
            latitudes_neg.append(record["location_latitude"])

            longitudes_neg.append(record["location_longitude"])


    one = m.scatter(longitudes_pos, latitudes_pos,
              latlon=True,  # Ta-da!
              marker='o', color='g',
              zorder=10)

    two = m.scatter(longitudes_neg, latitudes_neg,
              latlon=True,  # Ta-da!
              marker='o', color='r',
              zorder=10)

    plt.legend((one, two), ("Positive Sentiment", "Negative Sentiment"))
    plt.title("Spatial distribution of tweets - keyword : bts")


    plt.show()


spatial_tweet("test_db", "tweets", "bts")

#def line_graph1_tweet()


#a,b = senti_tweet("test_db", "tweets", "jesus")

#a,b = senti_news("test_db", "jesus")

#print(a,b)

#line_graph1_news("test_db", "bts")

#line_graph1_tweet("test_db", "tweets", "india")

#line_graph2("test_db", "tweets", "trump")

#histogram2()