from flask import Flask, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

app = Flask(__name__)

CORS(app)

@app.route("/")
def hello():
    return "Hi there"

sia = SIA()

@app.route('/receiver1', methods = ['POST'])
def worker1():
       
        data = request.get_data().lower()

	connection = MongoClient()

	db = connection["test_db"]

	collection = db["tweets"]

	db_record = db["tweets"].find_one({"ne_list" : data})

	if db_record == None:
		return "No records found"

        return db_record["text_body"]


@app.route('/receiver2', methods = ['POST'])
def worker2():

        data = request.get_data().lower()

        connection = MongoClient()

        db = connection["test_db"]

        collection = db["tweets"]

        db_record = db["tweets"].find_one({"ne_list" : data})

	if db_record == None:  
                return "No records found"


        return str(db_record["sentiment"]["compound"])

@app.route('/receiver3', methods = ['POST'])
def worker3():

        data = request.get_data().lower()

        connection = MongoClient()

        db = connection["news_db"]

        collection = db["news_overall"]

        db_record = db["news_overall"].find_one({"ne_list" : data})

	if db_record == None:  
                return "No records found"

        return db_record["text_body"]


@app.route('/receiver4', methods = ['POST'])
def worker4():

        data = request.get_data().lower()

        connection = MongoClient()

        db = connection["news_db"]

        collection = db["news_overall"]

        db_record = db["news_overall"].find_one({"ne_list" : data})

	if db_record == None:  
                return "No records found"


        return str(sia.polarity_scores(db_record["text_body"])["compound"])


if __name__ == "__main__":
    app.run(host="167.99.83.32", port=443, debug=True)
