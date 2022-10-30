from wtforms import Form, StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class TaskForm(Form):
    age = IntegerField('age', validators=[DataRequired()])
    mileage = IntegerField('mileage', validators=[DataRequired()])
    repairments = IntegerField('repairments', validators=[DataRequired()])
    brand_price = IntegerField('brand_price', validators=[DataRequired()])
