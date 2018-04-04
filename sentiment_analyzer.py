import json
from twython import Twython
import pymongo
from pymongo import MongoClient
import nltk
import re
from bs4 import BeautifulSoup
import datetime
import geopy
from geopy.geocoders import Nominatim
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()

def db_sent_analyzer(db_name, collection_name, body_name):

    k = 0

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    db_records = db[collection_name].find()

    for record in db_records:

        id = record["_id"]

        text = record[body_name]

        senti_dict = sia.polarity_scores(text)

        record["sentiment"] = senti_dict

        collection.update({"_id" : id}, { "$set": { "sentiment": senti_dict } } )

        k += 1

        print(k)


def adjust_ne(db_name, collection_name, body_name):

    k = 0

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    db_records = db[collection_name].find()

    for record in db_records:
        id = record["_id"]

        ne_list = record["ne_list"]

        ne_string = " ".join(ne_list)

        collection.update({"_id": id}, {"$set": {"ne_string": ne_string}})

        k += 1

        print(k)

def build_location_string_tweet(db_name, collection_name):

    geolocator = Nominatim(timeout=1000000)

    location_list = []

    k = 9950

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    db_records = db[collection_name].find()

    db_records.max_await_time_ms(1000000)

    db_records.max_time_ms(1000000)

    for record in db_records[9950:]:

        id = record["_id"]

        location = record['user']['location']

        """

        if location not in location_list:
            location_list.append(location)

        """

        geoloc = geolocator.geocode(location)

        if geoloc:
            collection.update({"_id": id}, {"$set": {"location_latitude" : geoloc.latitude, "location_longitude": geoloc.longitude}})
            location_list.append("f")

        k += 1

        print(k)
        print(len(location_list))

    return location_list

def count(db_name, collection_name):

    k = 0

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    db_records = db[collection_name].find()

    for record in db_records:

        if "location_latitude" in record:
            k += 1
            print(k)

#adjust_ne("test_db", "tweets", "a")

"""

location_list_corrected = []

for location in location_list:
    corrected = location.split(',')[-1].strip().lower()

    if corrected not in location_list_corrected:
        location_list_corrected.append(corrected)

print(len(location_list_corrected))

print(location_list_corrected)

"""


#db_sent_analyzer("test_db", "jesus",  "text_body")
adjust_ne("test_db", "bts",  "text_body")

