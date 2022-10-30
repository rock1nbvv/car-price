import sqlite3
import time

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

# [{'brand': 'Abarth', 'name': 'Fiat 500', 'price': 14699}, {'brand': 'Acura', 'name': 'ILX', 'price': 16000}, {'brand': 'Acura', 'name': 'MDX', 'price': 25075}, {'brand': 'Acura', 'name': 'RDX', 'price': 23500}, {'brand': 'Acura', 'name': 'RL', 'price': 7300}, {'brand': 'Acura', 'name': 'RLX', 'price': 25250}, {'brand': 'Acura', 'name': 'RSX', 'price': 5900}, {'brand': 'Acura', 'name': 'TL', 'price': 14450}, {'brand': 'Acura', 'name': 'TLX', 'price': 20900}, {'brand': 'Acura', 'name': 'TSX', 'price': 11000}, {'brand': 'Acura', 'name': 'ZDX', 'price': 17225}, {'brand': 'AION', 'name': 'V', 'price': 39900}, {'brand': 'Alfa Romeo', 'name': '159', 'price': 8250}, {'brand': 'Alfa Romeo', 'name': '164', 'price': 2500}, {'brand': 'Alfa Romeo', 'name': '166', 'price': 3600}, {'brand': 'Alfa Romeo', 'name': 'Brera', 'price': 17000}, {'brand': 'Alfa Romeo', 'name': 'Giulia', 'price': 27500}, {'brand': 'Alfa Romeo', 'name': 'Giulietta', 'price': 13325}, {'brand': 'Alfa Romeo', 'name': 'Stelvio', 'price': 34500}, {'brand': 'Aston Martin', 'name': 'DB9', 'price': 57000}, {'brand': 'Aston Martin', 'name': 'DBX', 'price': 193000}, {'brand': 'Aston Martin', 'name': 'Rapide', 'price': 123081}, {'brand': 'Aston Martin', 'name': 'Vantage', 'price': 103800}]
def parse_autos():
    brands = []

    print('fetching models dictionary')
    marks = requests.get(
        "https://developers.ria.com/auto/categories/:1/marks?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")
    limit = 5000
    index = 0

    try:
        for mark in json.loads(marks.text):
            if index >= limit:
                print('fetching models dictionary is done')
                break
            if index %8 ==0 and index >1:
                time.sleep(800)
            print("mark " + str(mark["value"]))
            carmodels = requests.get("https://developers.ria.com/auto/categories/1/marks/" + str(
                mark["value"]) + "/models?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn")

            for carmodel in json.loads(carmodels.text):
                print("model " + str(carmodel["value"]))
                prices = requests.get(
                    "https://developers.ria.com/auto/average_price?api_key=4mvHbKM5qP9FeuoE2QLYsWaEm8rKptSujd8MYAJn&marka_id=" + str(
                        mark["value"]) + "&model_id=" + str(carmodel["value"]) + "& gear_id=1&gear_id=2")
                if prices.json()["percentiles"] != 'NaN':
                    if prices.json()["percentiles"]["75.0"] != 'NaN':
                        index += 1
                        print(carmodel["name"], prices.json()["percentiles"]["75.0"])
                        # brand = json.dumps(
                        #     {"brand": mark["name"], "name": carmodel["name"], "price": prices.json()["percentiles"]["75.0"]})
                        # brands.append(brand)
                        brands.append({"brand": mark["name"], "name": carmodel["name"],
                                       "price": int(prices.json()["percentiles"]["75.0"])})
            print(brands)
    except:
        print("An exception occurred")
        time.sleep(800)
        parse_autos()

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
