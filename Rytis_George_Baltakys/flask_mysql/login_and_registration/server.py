from flask import *
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'letsbeoriginalnow'

mysql = MySQLConnector(app,'python')

@app.route('/')
def root():
	return render_template('index.html')

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
	query = "SELECT COUNT(*) AS count FROM lr_users WHERE email = :email"
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
	query = "INSERT INTO lr_users (email, fname, lname, pw_hash, created_at, updated_at) VALUES (:email, :fname, :lname, :pw_hash, NOW(), NOW())"
	# We'll then create a dictionary of data from the POST data received.
	data = {
					 'email': email,
					 'fname': fname,
					 'lname': lname,
					 'pw_hash': pw_hash
	}
	# run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	# log user in
	query = "SELECT id, email, fname, lname FROM lr_users WHERE email = :email"
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
	query = "SELECT id, email, fname, lname, pw_hash FROM lr_users WHERE email = :email"
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

app.run(debug=True)
