from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'makeitnew'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
		query = "SELECT * FROM friends"                           # define your query
		friends = mysql.query_db(query)                           # run query with query_db()
		return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
		# Write query to select specific user by id. At every point where
		# we want to insert data, we write ":" and variable name.
		query = "SELECT * FROM friends WHERE id = :specific_id"
		# Then define a dictionary with key that matches :variable_name in query.
		data = {'specific_id': friend_id}
		# Run query with inserted data.
		friends = mysql.query_db(query, data)
		# Friends should be a list with a single object,
		# so we pass the value at [0] to our template under alias one_friend.
		return render_template('edit.html', edit_friend=friends[0])

@app.route('/friends', methods=['POST'])
def create():
	email = request.form['email']

	formValid = True
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	if not EMAIL_REGEX.match(email):
		formValid = False
		flash('Invalid Email address')

	if not formValid:
		return redirect('/')

	# Write query as a string. Notice how we have multiple values
	# we want to insert into our query.
	query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
	# We'll then create a dictionary of data from the POST data received.
	data = {
					 'first_name': request.form['first_name'], 
					 'last_name':  request.form['last_name'],
					 'email': request.form['email']
				 }
	# Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
		query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
		data = {
						 'first_name': request.form['first_name'], 
						 'last_name':  request.form['last_name'],
						 'email': request.form['email'],
						 'id': friend_id
					 }
		mysql.query_db(query, data)
		return redirect('/')

@app.route('/friends/<friend_id>/delete')
def delete(friend_id):
		query = "DELETE FROM friends WHERE id = :id"
		data = {'id': friend_id}
		mysql.query_db(query, data)
		return redirect('/')

app.run(debug=True)
