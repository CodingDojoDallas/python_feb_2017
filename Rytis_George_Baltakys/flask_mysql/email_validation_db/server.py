from flask import *
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'keepitoriginal'

mysql = MySQLConnector(app,'emails')

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
	email = request.form['email']

	formValid = True
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	if not EMAIL_REGEX.match(email):
		formValid = False
		flash('Invalid Email address')

	if not formValid:
		return redirect('/')

	# email is Valid, save to database
	query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
	# We'll then create a dictionary of data from the POST data received.
	data = {
					 'email': email
				 }
	# Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	# get all emails addressed from the database
	query = "SELECT * FROM emails"

	emails = mysql.query_db(query)

	return render_template('emails.html', email=email, emails=emails)

@app.route('/delete/<email>')
def delete(email):
		query = "DELETE FROM emails WHERE id = :id"
		data = {'id': email}
		mysql.query_db(query, data)
		return redirect('/')

app.run(debug=True)
