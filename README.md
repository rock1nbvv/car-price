1. `python3 -m venv env`
   `source env/bin/activate`
   `python3 -m pip install -r requirements.txt`

2. `export FLASK_APP=app`
   `flask shell`

3. `from app import db`
   `from models import Task`
   `from models import CarBrands`
   `db.create_all()`
   run `brand.sql`

4. optional:
   ~~t1 = Task(title='New task 1')~~
   ~~t2 = Task(title='New task 2')~~

   ~~db.session.add(t1)~~
   ~~db.session.add(t2)~~
   db.session.commit()

5. `flask run`