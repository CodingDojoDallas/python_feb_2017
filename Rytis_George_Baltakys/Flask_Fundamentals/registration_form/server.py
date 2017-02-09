from flask import *
import re
app = Flask(__name__)
app.secret_key = 'alskdjrop23w8fjawf'

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	password = request.form['password']
	passwordc = request.form['passwordc']

	formValid = True
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

	if len(fname) == 0 or len(lname) == 0 or len(email) == 0 or len(password) == 0 or len(passwordc) == 0 :
		formValid = False
		flash('Please fill in all fields')
	if not fname.isalpha() or not lname.isalpha():
		formValid = False
		flash('Your name should include only letters')
	if not EMAIL_REGEX.match(email):
		formValid = False
		flash('Invalid Email address')
	if len(password) < 8:
		formValid = False
		flash('Your password should be 8 or more characters')
	if password != passwordc:
		formValid = False
		flash('Your passwords must match')

	if not formValid:
		return redirect('/')

	return render_template('user.html', fname=fname, lname=lname, email=email)


app.run(debug=True)