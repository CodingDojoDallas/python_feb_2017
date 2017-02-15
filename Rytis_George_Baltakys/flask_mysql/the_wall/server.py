from flask import *
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt
import datetime
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'pinkfloyd'

mysql = MySQLConnector(app,'thewall')

@app.route('/')
def root():

	posts = []

	# if logged in, retrieve the wall
	if 'user' in session:
		# get the posts
		query = "SELECT p.id AS id, post, p.created_at, fname, lname, email FROM posts p JOIN users u ON u.id = p.user_id ORDER BY created_at DESC"
		posts = mysql.query_db(query)

		# get comments for each post
		for post in posts:
			query = "SELECT c.id AS id, comment, c.created_at, fname, lname, email FROM comments c JOIN users u ON u.id = c.user_id WHERE post_id = :postid ORDER BY created_at"
			print query
			data = {
								'postid': post['id']
			}
			comments = mysql.query_db(query, data)
			post['comments'] = comments

	return render_template('index.html', posts=posts)

@app.route('/register', methods=['POST'])
def register():
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	password = request.form['pass']
	passwordc = request.form['passc']

	formValid = True
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	if len(fname) == 0 or len(lname) == 0 or len(email) == 0 or len(password) == 0 or len(passwordc) == 0:
		formValid = False
		flash('Please fill in all fields')
	if not fname.isalpha() or not lname.isalpha():
		formValid = False
		flash('Your name should include only letters')
	if len(fname) < 2 or len(lname) < 2:
		formValid = False
		flash('Your name should be at least 2 characters')
	if not EMAIL_REGEX.match(email):
		formValid = False
		flash('Invalid Email address')
	if len(password) < 8:
		formValid = False
		flash('Your password should be 8 or more characters')
	if password != passwordc:
		formValid = False
		flash('Your passwords must match')

	# check if user already registered
	query = "SELECT COUNT(*) AS count FROM users WHERE email = :email"
	data = {
						'email': email
	}
	returnData = mysql.query_db(query, data)
	count = returnData[0]['count'];

	if count > 0:
		formValid = False
		flash('This email address is already registered')

	if not formValid:
		return redirect('/')

	# generate password hash
	pw_hash = bcrypt.generate_password_hash(password)

	# form data is Valid, save to database
	query = "INSERT INTO users (email, fname, lname, pw_hash, created_at, updated_at) VALUES (:email, :fname, :lname, :pw_hash, NOW(), NOW())"
	# we'll then create a dictionary of data from the POST data received.
	data = {
					 'email': email,
					 'fname': fname,
					 'lname': lname,
					 'pw_hash': pw_hash
	}
	# run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	# log user in
	query = "SELECT id, email, fname, lname FROM users WHERE email = :email"
	data = {
						'email': email
	}
	returnData = mysql.query_db(query, data)
	session['user'] = returnData[0]

	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['pass']

	formValid = True
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	if len(email) == 0 or len(password) == 0:
		formValid = False
		flash('Please fill in the username and password')
	if not EMAIL_REGEX.match(email):
		formValid = False
		flash('Invalid Email address')

	if not formValid:
		return redirect('/')

	# retrieve user info from db
	query = "SELECT id, email, fname, lname, pw_hash FROM users WHERE email = :email"
	data = {
						'email': email
	}
	returnData = mysql.query_db(query, data)
	if len(returnData) == 0:
		flash("The email and password doesn't match")
		return redirect('/')

	# check if the password matches
	if bcrypt.check_password_hash(returnData[0]['pw_hash'], password):
		# log user in
		returnData[0].pop('pw_hash', None)
		session['user'] = returnData[0]
	else:
		flash("The email and password doesn't match")

	return redirect('/')

@app.route('/logout')
def logout():
	session.clear()

	return redirect('/')

@app.route('/post', methods=['POST'])
def post():

	post = request.form['posting']

	formValid = True

	if len(post) == 0:
		formValid = False
		flash('Please fill in your post')

	if not formValid:
		return redirect('/')

	# save post to database
	query = "INSERT INTO posts (user_id, post, created_at, updated_at) VALUES (:userid, :post, NOW(), NOW())"

	data = {
					 'userid': session['user']['id'],
					 'post': post
	}

	# run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	return redirect('/')

@app.route('/comment', methods=['POST'])
def comment():
	print 'here'
	comment = request.form['comment']
	postid = request.form['postid']
	print 'there'
	formValid = True

	if len(comment) == 0:
		formValid = False
		flash('Please fill in your comment')

	if not formValid:
		return redirect('/')

	# save post to database
	query = "INSERT INTO comments (post_id, user_id, comment, created_at, updated_at) VALUES (:postid, :userid, :comment, NOW(), NOW())"

	data = {
					'postid': postid,
					'userid': session['user']['id'],
					'comment': comment
	}

	# run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	return redirect('/')

@app.route('/comment/<id>/delete')
def delcomment(id):
	query = "DELETE FROM comments WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query, data)

	return redirect('/')

@app.route('/post/<id>/delete')
def delpost(id):
	query = "DELETE FROM comments WHERE post_id = :id; DELETE FROM posts WHERE id = :id"
	data = {'id': id, 'id': id}
	mysql.query_db(query, data)

	return redirect('/')

app.run(debug=True)
