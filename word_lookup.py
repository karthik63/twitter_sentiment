import json
from twython import Twython
import pymongo
import dateutil.parser
import datetime
from pymongo import MongoClient
import pytz
import nltk
import re
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def lookup_tweet(db_name, collection_name, body_name, word, location_field = None, location = None, time_field = None, time = None):
    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]


    if location_field == None and time_field == None:
        records_db = collection.find({"ne_string":{"$regex" : "." + "*" + word + "." + "*"}})

    if location_field != None and time_field == None:
        records_db = collection.find({"ne_string":{"$regex" : "." + "*" + word + "." + "*"}})


    sentiscore = 0

    number = 0

    for record in records_db:

        number += 1

        sentiscore += record["sentiment"]["compound"]

    if number == 0:
        return False, False

    else:
        return number, sentiscore / number

def lookup_news(db_name, collection_name, body_name, word, location_field = None, location = None, time_field = None, time = None):
    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]


    if location_field == None and time_field == None:
        records_db = collection.find({"ne_string":{"$regex" : "." + "*" + word + "." + "*"}})

    if location_field != None and time_field == None:
        records_db = collection.find({"ne_string":{"$regex" : "." + "*" + word + "." + "*"}})


    sentiscore = 0

    number = 0

    for record in records_db:

        number += 1

        sentiscore += record["sentiment"]["compound"]

    if number == 0:
        return False, False

    else:
        return number, sentiscore / number

def date_query(db_name, collection_name, gte, lt):
    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    query_records = collection.find({"datetime_format" : {"$gte" : gte, "$lt" : lt}})

    number = 0

    sentiscore = 0

    for record in query_records:
        number += 1

        sentiscore += record["sentiment"]["compound"]

    if number == 0:
        return  0, 0

    else:
        return number, sentiscore / number


def alter_date_news(db_name, collection_name):

    k = 0

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    db_records = db[collection_name].find()

    db_records.max_await_time_ms(1000000)

    db_records.max_time_ms(1000000)

    mindate = datetime.datetime(3000, 2, 2, 0 , 0, 0, tzinfo=pytz.UTC)
    maxdate = datetime.datetime(1000, 2, 2, 0, 0, 0, tzinfo=pytz.UTC)

    for record in db_records:

        id = record["_id"]

        date_string = record["dateTime"]

        datetime_format = dateutil.parser.parse(date_string)

        if datetime_format > maxdate:
            maxdate = datetime_format

        if datetime_format < mindate:
            mindate = datetime_format

        collection.update({"_id": id}, {"$set": {"datetime_format": datetime_format}})

        k += 1

        print(k)

    print(maxdate)
    print(mindate)

    return 0

def alter_date_tweet(db_name, collection_name):

    k = 0

    connection = MongoClient()

    db = connection[db_name]

    collection = db[collection_name]

    db_records = db[collection_name].find()

    db_records.max_await_time_ms(1000000)

    db_records.max_time_ms(1000000)

    mindate = datetime.datetime(3000, 2, 2, 0 , 0, 0, tzinfo=pytz.UTC)
    maxdate = datetime.datetime(1000, 2, 2, 0, 0, 0, tzinfo=pytz.UTC)

    for record in db_records:

        id = record["_id"]

        date_string = record["created_at"]

        datetime_format = dateutil.parser.parse(date_string)

        print(datetime_format)

        if datetime_format > maxdate:
           maxdate = datetime_format

        if datetime_format < mindate:
           mindate = datetime_format

        collection.update({"_id": id}, {"$set": {"datetime_format": datetime_format}})

        k += 1

        print(k)

    print(maxdate)
    print(mindate)

    return 0

#alter_date_tweet("test_db", "tweets")

#date_query("test_db", "news_overall")

#lookup_tweet("test_db", "tweets",  "text_body", "happy")



