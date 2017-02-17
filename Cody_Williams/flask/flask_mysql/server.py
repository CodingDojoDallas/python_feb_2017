from flask import *
from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, 'full_friendsies')

@app.route('/')
def index():
	return 'hello world'

app.run(debug=True)