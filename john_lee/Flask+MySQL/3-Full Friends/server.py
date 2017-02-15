from flask import *
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'covertkey'
mysql = MySQLConnector(app, 'full_friends')

@app.route("/")
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    data = {
        'friends': friends,
    }
    return render_template('index.html', data=data)

@app.route("/friends", methods=['POST'])
def create_user():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    values = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    mysql.query_db(query, values)
    return redirect('/')

@app.route("/friends/<id>/edit")
def edit_user(id):
    query = 'SELECT * FROM friends WHERE id = :id'
    values = {'id': id}
    friend = mysql.query_db(query, values)
    data = {'friend':friend}
    return render_template('edit.html', data=data)

@app.route('/friends/<id>', methods=['POST'])
def update_friend(id):
    query = 'UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id'
    values = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email': request.form['email'],
        'id': id
    }
    mysql.query_db(query, values)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    values = {'id': id}
    friend = mysql.query_db(query, values)
    return redirect('/')

app.run(debug=True)
