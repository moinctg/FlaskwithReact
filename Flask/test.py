from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/form2', methods=["POST"])
def form2_api():
    print(request.json)
    response = {"status" : "Succesfully upload"}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)