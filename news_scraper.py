import nltk
from eventregistry import *
import json
import dateutil.parser
from pymongo import MongoClient

connection = MongoClient()

db = connection['test_db']

news_db = db['news_overall']

bts_db = db['bts']

jesus_db = db['jesus']

trump_db = db['trump']

india_db = db['india']

easter_db = db['easter']

toplist = ['science' 'jesus' 'trump' 'bts' 'india' 'easter' 'stephen' 'cambridge' 'british' 'no']

er = EventRegistry(apiKey="2dbe21a5-0251-4c40-a47f-2f294372fce7")

q = QueryArticlesIter(keywords="easter", keywordsLoc="title")

i = 0

for news_dict in q.execQuery(er, sortBy="date", lang="eng"):

    if news_dict["lang"] == "eng":

        text = news_dict['body']

        text = re.sub(r'http\S*', " ", text)

        text = text.replace('\n', ' ')

        sentences = nltk.sent_tokenize(text)

        ne_list = []

        for sentence in sentences:

            pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
            ne = nltk.ne_chunk(pos)

            for chunk in ne:

                if hasattr(chunk, 'label'):
                    ne_list.append(chunk[0][0].lower())

        #print(ne_list)

        news_dict['ne_list'] = ne_list
        news_dict["text_body"] = text

        easter_db.insert(news_dict)

        news_db.insert(news_dict)

        i += 1

        print(i)

    if i >=500:
        break



q = QueryArticlesIter(keywords="trump", keywordsLoc="title")

i = 0

for news_dict in q.execQuery(er, sortBy="date", lang="eng"):

    # print(json.dumps(news_dict))

    if news_dict["lang"] == "eng":

        text = news_dict['body']

        text = re.sub(r'\'http\S*', " ", text)

        text = text.replace('\n', ' ')

        sentences = nltk.sent_tokenize(text)

        ne_list = []

        for sentence in sentences:

            pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
            ne = nltk.ne_chunk(pos)

            for chunk in ne:

                if hasattr(chunk, 'label'):
                    ne_list.append(chunk[0][0].lower())

        #print(ne_list)

        news_dict['ne_list'] = ne_list
        news_dict["text_body"] = text

        trump_db.insert(news_dict)

        news_db.insert(news_dict)

        i += 1

        print(i)

    if i >= 500:
        break


q = QueryArticlesIter(keywords="bts", keywordsLoc="title")

i = 0

for news_dict in q.execQuery(er, sortBy="date", lang="eng"):

    # print(json.dumps(news_dict))

    if news_dict["lang"] == "eng":

        text = news_dict['body']

        text = re.sub(r'http\S*', " ", text)

        text = text.replace('\n', ' ')

        sentences = nltk.sent_tokenize(text)

        ne_list = []

        for sentence in sentences:

            pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
            ne = nltk.ne_chunk(pos)

            for chunk in ne:

                if hasattr(chunk, 'label'):
                    ne_list.append(chunk[0][0].lower())

        #print(ne_list)


        news_dict['ne_list'] = ne_list
        news_dict["text_body"] = text

        bts_db.insert(news_dict)

        news_db.insert(news_dict)

        i += 1

        print(i)

    if i >= 500:
        break


q = QueryArticlesIter(keywords="jesus", keywordsLoc="title")

i = 0

for news_dict in q.execQuery(er, sortBy="date", lang="eng"):

    if news_dict["lang"] == "eng":

        text = news_dict['body']

        text = re.sub(r'http\S*', " ", text)

        text = text.replace('\n', ' ')

        sentences = nltk.sent_tokenize(text)

        ne_list = []

        for sentence in sentences:

            pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
            ne = nltk.ne_chunk(pos)

            for chunk in ne:

                if hasattr(chunk, 'label'):
                    ne_list.append(chunk[0][0].lower())

        #print(ne_list)


        news_dict['ne_list'] = ne_list
        news_dict["text_body"] = text

        jesus_db.insert(news_dict)

        news_db.insert(news_dict)

        i += 1

        print(i)

    if i >= 500:
        break


q = QueryArticlesIter(keywords="india", keywordsLoc="title")

i = 0

for news_dict in q.execQuery(er, sortBy="date", lang="eng"):

    if news_dict["lang"] == "eng":

        text = news_dict['body']

        text = re.sub(r'http\S*', " ", text)

        text = text.replace('\n', ' ')

        sentences = nltk.sent_tokenize(text)

        ne_list = []

        for sentence in sentences:

            pos = nltk.tag.pos_tag(nltk.word_tokenize(sentence))
            ne = nltk.ne_chunk(pos)

            for chunk in ne:

                if hasattr(chunk, 'label'):
                    ne_list.append(chunk[0][0].lower())

        #print(ne_list)


        news_dict['ne_list'] = ne_list
        news_dict["text_body"] = text

        india_db.insert(news_dict)

        news_db.insert(news_dict)

        i += 1

        print(i)

    if i >= 500:
        break
