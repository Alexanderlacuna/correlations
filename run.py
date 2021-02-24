from database import create_app
from sqlalchemy import create_engine

import pymysql
from flask import g

app = create_app({})

engine = create_engine("mysql+pymysql://kabui:1234@localhost/db_webqtl")
SQL_URI = "mysql+pymysql://kabui:1234@localhost/db_webqtl"
c =engine.connect()

# from database import db
@app.before_request
def connect_db():
    print("@app.before_request connect_db")
    db = getattr(g, '_database', None)
    if db is None:
        print("Get new database connector")
        g.db = g._database = create_engine(SQL_URI, encoding="latin1")
        print(g.db)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        print("remove db_session")
        db_session.remove()
        g.db = None


@app.route("/hello")
def home():
    print(g.db)

    return "hello"
	# print(c)
	# results = c.execute("SELECT * FROM  Docs;")
	# print("*******",results.fetchall())
	
if __name__ == '__main__':
	app.run()