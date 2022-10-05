import datetime

from flask import Flask, request, jsonify
from pymongo import MongoClient
import configparser

Config = configparser.ConfigParser()
Config.read("config.ini")

app = Flask(__name__)

mongodb_client = MongoClient(Config.get("APP", "ATLAS_URI"))
db = mongodb_client["checkins"]
collection = db["checkins"]



@app.route('/record')
def record():
    record_return = collection.find({})
    r = [{"timestamp": x["timestamp"], "ip": x["ip"]} for x in record_return]
    return jsonify(r), 200


# I protest. This is not a RESTful implementation, man
@app.route('/record/add', methods=["POST"])
def record_add():

    new_record = {
        "timestamp": datetime.datetime.now(),
        "ip": request.remote_addr
    }
    collection.insert_one(new_record)
    return "", 200


if __name__ == "__main__":
    app.run(debug=True, port=int(Config.get("APP", "PORT")))
