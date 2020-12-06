from flask import Flask
from flask import request
from flask import jsonify
import json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://test1234:test1234@cluster1.fpenn.mongodb.net/testdb?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test', methods=["POST"])
def test_api():
    data = request.json
    mongo.db.user.save(data)
    print(request.json)
    response = {"status" : "ufbh"}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)