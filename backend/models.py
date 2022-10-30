from dataclasses import dataclass
from datetime import datetime

import app


@dataclass
class Task(app.db.Model):

    id: int
    age: int
    mileage: int
    repairments: int
    documents: bool
    date: datetime
    completed: bool
    brand: str
    name: str
    est_price: int

    id = app.db.Column(app.db.Integer(), primary_key=True)
    age = app.db.Column(app.db.Integer())
    mileage = app.db.Column(app.db.Integer())
    repairments = app.db.Column(app.db.Integer())
    brand = app.db.Column(app.db.String(100))
    name = app.db.Column(app.db.String(100))
    documents = app.db.Column(app.db.Boolean())
    date = app.db.Column(app.db.DateTime(), default=datetime.now())
    completed = app.db.Column(app.db.Boolean(), default=False)
    est_price = app.db.Column(app.db.Integer())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Task id: {self.id} - {self.est_price}'


@dataclass
class Brand(app.db.Model):
    id: int
    brand: str
    name: str
    price: int

    id = app.db.Column(app.db.Integer(), primary_key=True)
    brand = app.db.Column(app.db.String(100))
    name = app.db.Column(app.db.String(100))
    price = app.db.Column(app.db.Integer())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<CarBrand id: {self.id} - {self.brand} - {self.name} - {self.price}'
