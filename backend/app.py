from flask import Flask, Response
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from flask_cors import CORS

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from model import model
from carEvaluation import carEvaluation
from config import Config

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
import models

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def index():
    return "hello, world"


@app.route('/api/getCarHistory', methods=['GET'])
def get():
    carHistory = models.Task.query.all()
    return jsonify(carHistory)


@app.route('/api/getBrands', methods=['GET'])
def get_brands():
    brands = models.Brand.query.all()
    return jsonify(brands)


@app.route('/api/evaluate', methods=['POST'])
def get_price():
    fuzzy_model = model()
    user_input = request.get_json()
    car_condition = carEvaluation(int(user_input["age"]), int(user_input["mileage"]), int(user_input["repairments"]),fuzzy_model[0],fuzzy_model[1], fuzzy_model[2])
    est_price = user_input["selectedCarObj"]["price"] * car_condition[0]*0.1
    if str(user_input["areDocsInOrder"]) != 'True':
        est_price *= 0.2

    response = {"price": est_price}
    task = models.Task(
        age=user_input["age"],
        mileage=user_input["mileage"],
        repairments=user_input["repairments"],
        brand=user_input["selectedCarObj"]["brand"],
        name=user_input["selectedCarObj"]["name"],
        documents=user_input["areDocsInOrder"],
        est_price=response["price"])
    db.session.add(task)
    db.session.commit()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
