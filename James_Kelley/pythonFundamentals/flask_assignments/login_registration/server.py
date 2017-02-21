from flask import *
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)

mysql = MySQLConnector(app, 'login_registration')
bcrypt = Bcrypt(app)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/users', methods=['post'])
def create_user():
	if request.form['password'] != request.form['password_confirmation']:
			flash('Your password does not match.')
			return redirect('/')
	query = 'INSERT INTO users (email, password, updated_at, created_at) VALUES (:email, :password, NOW(), NOW());'
	values = {
	'email': request.form['email'],
	'password':  bcrypt.generate_password_hash(request.form['password']),
	}
	user_id = mysql.query_db(query, values)
	session['user_id'] = user_id 
	return redirect('/success')

@app.route('/success')
def success():
	query = 'SELECT * FROM users WHERE id = :id;'
	values = {'id' : session['user_id']}
	user = mysql.query_db(query, values)
	data = {
		'user': user[0], 
	}

	return render_template('success.html', data=data)

@app.route('/session', methods=['post'])
def login_user():
	query = 'SELECT * from users WHERE email = :email;'
	values = {
		'email': request.form['email'],
	}
	user = mysql.query_db(query, values)
	if len(user) != 0 and bcrypt.check_password_hash(user[0]['password'], request.form['password']):
		session['user_id'] = user[0]['id']
		return redirect('/success')
	else: 
		flash('Invalid Credentials.')
		return redirect('/')
	

app.run(debug=True)