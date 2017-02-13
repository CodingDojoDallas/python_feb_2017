from flask import Flask, session, render_template, redirect, flash, request
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector


app = Flask(__name__)
app.secret_key = 'specialpassword'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'flask_login_reg_27')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create():
	name = request.form['name']
	email = request.form['email']
	password = request.form['password']

	is_valid = True

	if len(name) == 0:
		flash('Name cannot be blank', 'registration')
		is_valid = False
	if len(email) == 0:
		flash('Email cannot be blank', 'registration')
		is_valid = False
	#use regex to confirm the email is valid
	if len(password) < 3:
		flash('Password must be at least three characters', 'registration')
		is_valid = False

	if is_valid:
		#save into DB
		hashed_pw = bcrypt.generate_password_hash(password)
		query = 'INSERT INTO users (name, email, password, created_at, updated_at) VALUES(:name, :email, :password, NOW(), NOW());'
		data = {
			'name': name,
			'email': email,
			'password': hashed_pw,
		}
		print '*'*100
		user_id = mysql.query_db(query, data)
		session['user_id'] = user_id
		return redirect('/success')
	else:
		#redirect to registration page and show errors
		return redirect('/')


@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']

	query = 'SELECT * FROM users WHERE email = :email;'
	data = {'email': email}

	user = mysql.query_db(query, data)

	if user and bcrypt.check_password_hash(user[0]['password'], password):
		session['user_id'] = user[0]['id']
		return redirect('/success')
	else:
		flash('Invalid credentials.', 'login')
		return redirect('/')

@app.route('/success')
def dashboard():
	if 'user_id' not in session:
		return redirect('/')
	else:
		return render_template('success.html')


@app.route('/logout', methods=['POST'])
def logout():
	session.clear()
	return redirect('/')

app.run(debug=True)





