from flask import *
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'soverysecret'

mysql = MySQLConnector(app, 'full_friends')

@app.route("/")
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	data = {
	'friends': friends,
	}
	return render_template('index.html', data=data)

@app.route("/users", methods=['POST'])
def create_user():
	query = "INSERT INTO friends (name, created_at, updated_at) VALUES (:name, NOW(), NOW())" 
	values = {
		'name': request.form['name']
	}
	mysql.query_db(query, values)
	return redirect('/')

@app.route("/friends/<id>/edit")
def edit_user(id):
	query = 'SELECT * FROM friends WHERE id = :id'
	values = {
		'id': id
	}
	friend = mysql.query_db(query, values)
	data = {
		'friend' : friend
	}
	return render_template('edit_user.html', data=data)

@app.route('/friends/<id>', methods=['POST'])
def updated_friend(id):
	query = 'UPDATE friends SET name = :name WHERE id = :id;'
	values = {
	'name': request.form['name'],
	'id': id
	}
	mysql.query_db(query, values)
	return redirect('/')

app.run(debug=True)