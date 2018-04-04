import json
from twython import Twython
import pymongo
from pymongo import MongoClient
import nltk
import re
from bs4 import BeautifulSoup

API_KEY = "vVQJD8iOQ1DaNk7geYg9ZSYBV"
API_KEY_SECRET = "r3yljFQMpop9v3M6lnAEfNGUsMyPnw2tNdn4HNo3M6cJazmx0O"
TOKEN = "980046821086019584-bMbv5stzj4wja8yJiobD6xA7W7qcrLE"
TOKEN_SECRET = "gvm4jcTV2EljA78Nu8Vv7W1zl2pDw6fl0woutZjiQ76Zl"

twitter = Twython(API_KEY, API_KEY_SECRET, TOKEN, TOKEN_SECRET)

connection = MongoClient()

db = connection['test_db']

data = twitter.search(q="the", count = "100", lang="en", result="popular", tweet_mode="extended")

metadata = data["search_metadata"]

data = data["statuses"]

for j in range(100):

    print(j)

    for i in data:

        if "retweeted_status" in i:
            text = (BeautifulSoup(i["retweeted_status"]["full_text"], 'lxml').get_text())

            text = text.replace('@', '')
            text = text.replace('#', '')

            text = re.sub(r'http\S*', " ", text)

            #print(text)

            sentences = nltk.sent_tokenize(text)

            ne_list = []

            for sentence in sentences:

                pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
                ne =  nltk.ne_chunk(pos)

                for chunk in ne:

                    if hasattr(chunk, 'label'):

                        ne_list.append(chunk[0][0].lower())

            #print(ne_list)

            i["ne_list"] = ne_list
            i["_id"] = i['id_str']
            i["text_body"] = text

            db['tweets'].insert(i)

            #print("\n")

        else:
            text = (BeautifulSoup(i["full_text"], 'lxml').get_text())

            text = text.replace('@', '')
            text = text.replace('#', '')

            text = re.sub(r'http\S*', " ", text)

            #print(text)

            sentences = nltk.sent_tokenize(text)

            ne_list = []

            for sentence in sentences:

                pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
                ne = nltk.ne_chunk(pos)

                for chunk in ne:

                    if hasattr(chunk, 'label'):
                        ne_list.append(chunk[0][0].lower())

            #print(ne_list)

            i["ne_list"] = ne_list
            i["_id"] = i['id_str']
            i["text_body"] = text

            db['tweets'].insert(i)

            #print("\n")

    next_field = metadata["next_results"]

    max_id = next_field.split('&')[0][8:]

    data = twitter.search(q="the", include_entities=1, max_id=max_id, lang="en", count="100", tweet_mode="extended", result="popular")

    metadata = data["search_metadata"]

    data = data["statuses"]