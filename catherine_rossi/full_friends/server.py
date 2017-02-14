from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends_db')

#display all of the friends from my db on the index.html page
@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM friends")
	#print friends
	return render_template('index.html', all_friends=friends)

#handles the add friend form submit and creates the firend in the DB  
@app.route('/friends', methods=['POST'])
def create():

    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    #creates a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

#@app.route('/friends/<friend_id>')
@app.route("/friends/<id>/edit") # will look like this: /friends/8/edit in the URL
def edit(id):
    # Write query to select specific friend id. 
    #SQL statement
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': id}
    # Run query with selected data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('edit.html', one_friend=friends[0])   

# will handle the edit form submit & update the db w/ the friends name
     
@app.route("/friends/<id>", methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route("/friends/<id>/delete", methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')    



app.run(debug=True)
