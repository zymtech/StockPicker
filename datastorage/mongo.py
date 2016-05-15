import pymongo
import json
import time


def writetomongo(df):
    connection = pymongo.MongoClient('127.0.0.1',port=27017)
    database = "stock"
    collection = "profit" + time.strftime("%Y-%m-%d",time.localtime())
    connection[database][collection].insert(json.loads(df.to_json(orient='records')))

