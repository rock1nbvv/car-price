from flask import Flask, Response
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from flask_cors import CORS

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

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


@app.route('/api/getTasks', methods=['GET'])
def get():
    tasks = [{'taskId': '1', 'title': 'First Task'}, {'taskId': '2', 'title': 'Second Task'}]
    return jsonify(tasks)


@app.route('/api/getBrands', methods=['GET'])
def get_brands():
    brands = models.Brand.query.all()
    return jsonify(brands)


@app.route('/api/evaluate', methods=['POST'])
def get_price():
    # TODO calculate final predicted price (params: fuzzy response, avg price, areDocsOk etc)

    # TODO create Table with Evaluations History, add result to this table, create History.vue component and display
    #  everything there

    user_input = request.get_json()
    print(user_input)

    response = {"price": 5353}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
