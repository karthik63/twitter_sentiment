import json
from twython import Twython
import pymongo
from pymongo import MongoClient
import sys
print(sys.executable)
import nltk
import textmining
import numpy as np
import re
from bs4 import BeautifulSoup


connection = MongoClient()

db = connection['test_db']

a = db['tweets'].find()

tdm = textmining.TermDocumentMatrix()

for record in a:

   ne_words = ' '.join(record['ne_list'])

   tdm.add_doc(ne_words)

tdm.write_csv("test_file", cutoff=0)

with open('test_file', 'r') as file:
    line = file.readline()

    wordlist = line.strip().split(',')

print(wordlist)

print(len(wordlist))

with open('test_file', 'r') as file:
    d = file.readlines()

with open('test_file_new', 'w+') as file:
    for line in d[1:]:
        file.write(line)

tdm_matrix = np.loadtxt('test_file_new', delimiter=',')

occurences = tdm_matrix.sum(0)

sorted_indices = np.argsort(occurences)

sorted_indices = sorted_indices[::-1]

wordlist = np.array(wordlist)

print(wordlist[sorted_indices][:10])

with open('test_file_new', 'a') as file:
    file.write(' '.join(wordlist[sorted_indices][:10]))