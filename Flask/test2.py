from flask import Flask
from flask import request
from flask import jsonify
import json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.first_name}', '{self.last_name}')"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/FormDesign', methods=["POST"])
def FormDesign_api():
    data = request.json
    data = json.loads(data)
    print(data)
    #reg = Register(data[''])
    response = {"status" : "Succesfully upload"}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)