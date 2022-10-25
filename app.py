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
    brands = models.Brand.query.all()
    limit = 10
    index = 0
    if len(brands) < limit:
        marks = requests.get(
            "https://developers.ria.com/auto/categories/:1/marks?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")

        for mark in json.loads(marks.text):
            if index >= limit:
                break
            print("mark " + str(mark["value"]))
            carmodels = requests.get("https://developers.ria.com/auto/categories/1/marks/" + str(
                mark["value"]) + "/models?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")

            for carmodel in json.loads(carmodels.text):
                print("model " + str(carmodel["value"]))
                prices = requests.get(
                    "https://developers.ria.com/auto/average_price?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn&marka_id=" + str(
                        mark["value"]) + "&model_id=" + str(carmodel["value"]) + "& gear_id=1&gear_id=2")

                if prices.json()["percentiles"]["75.0"] != 'NaN':
                    index += 1
                    print(carmodel["name"], prices.json()["percentiles"]["75.0"])
                    brand = models.Brand(name=carmodel["name"], price=prices.json()["percentiles"]["75.0"])
                    db.session.add(brand)
                    db.session.commit()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)

    return render_template('index.html')


@app.route('/brands')
def get_brands():
    brands = models.Brand.query.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(brands)

    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_task():
    user_input = request.get_json()
    form = TaskForm(data=user_input)
    if form.validate():
        task = models.Task(taskTitle=form.taskTitle.data,
                           age=form.age.data,
                           mileage=form.mileage.data,
                           repairments=form.repairments.data,
                           brand_price=form.brand_price.data,
                           documents=form.documents.data)
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
