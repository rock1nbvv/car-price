import sqlite3

import requests
import json
from pathlib import Path


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn


def parse_autos():
    brands = []

    print('fetching models dictionary')
    marks = requests.get(
        "https://developers.ria.com/auto/categories/:1/marks?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")
    limit = 20
    index = 0
    for mark in json.loads(marks.text):
        if index >= limit:
            print('fetching models dictionary is done')
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
                # brand = json.dumps(
                #     {"brand": mark["name"], "name": carmodel["name"], "price": prices.json()["percentiles"]["75.0"]})
                # brands.append(brand)
                brands.append({"brand": mark["name"], "name": carmodel["name"], "price": int(prices.json()["percentiles"]["75.0"])})
    print(brands)

    # add to db

    print("Adding to DB")

    database = Path(__file__).parents[1] / 'db.sqlite'

    if database.is_file():
        conn = create_connection(database)
        c = conn.cursor()

        c.execute('DELETE FROM brand;', );

        for brand in brands:
            print(brand)
            c.execute("INSERT INTO brand(brand,name,price) VALUES(?,?,?)",
                      (brand['brand'], brand['name'], brand['price']))
        conn.commit()
        conn.close()
    else:
        raise Exception('Wrong database path')


if __name__ == '__main__':
    parse_autos()
