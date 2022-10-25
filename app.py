import json

from flask import Flask, Response
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
import requests

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from config import Config

load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
import models
from forms import TaskForm


@app.route('/')
def index():
    tasks = models.Task.query.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)

    return render_template('index.html')


@app.route('/brands')
def get_brands():
    brands = models.Brand.query.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(brands)

    return render_template('index.html')


@app.route("/get-models")
def proxy_example():
    marks = requests.get(
        "https://developers.ria.com/auto/categories/:1/marks?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")

    for mark in json.loads(marks.text):
        print("mark " + str(mark["value"]))
        models = requests.get("https://developers.ria.com/auto/categories/1/marks/" + str(
            mark["value"]) + "/models?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")

        for model in json.loads(models.text):
            print("model " + str(model["value"]))
            prices = requests.get(
                "https://developers.ria.com/auto/average_price?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn&marka_id=" + str(mark["value"]) + "&model_id=" + str(model["value"]) + "& gear_id=1&gear_id=2")

            # for price in prices.json()["percentiles"]["75.0"]:
            print(prices.json()["percentiles"]["75.0"])

    return Response(
        marks.text,
        status=marks.status_code,
        content_type=marks.headers['content-type']
    )

    @app.route('/create', methods=['POST'])
    def create_task():
        user_input = request.get_json()

        form = TaskForm(data=user_input)  # todo parse not only task.title but car object

        if form.validate():
            task = models.Task(title=form.title.data)

            db.session.add(task)
            db.session.commit()

            return jsonify(task)

        return redirect(url_for(index))

    @app.route('/delete', methods=['POST'])
    def delete_task():
        task_id = request.get_json().get('id')
        task = models.Task.query.filter_by(id=task_id).first()

        db.session.delete(task)
        db.session.commit()

        return jsonify({'result': 'Ok'}), 200

    @app.route('/complete', methods=['POST'])
    def complete_task():
        task_id = request.get_json().get('id')
        task = models.Task.query.filter_by(id=task_id).first()

        task.completed = True

        db.session.add(task)
        db.session.commit()

        return jsonify({'result': 'Ok'}), 200

    if __name__ == '__main__':
        app.run()
