from flask import Flask, render_template, flash, session, redirect, request

import random

app = Flask(__name__)
app.secret_key = 'somethingsecret'

@app.route('/')
def index():
	data = 'hello world'
	# session.clear()
	return render_template('index.html', data=data)

@app.route('/users', methods=['POST'])
def create_user():
	#valiate the input
	isValid = True
	name = request.form['name']
	if len(name) < 3:
		flash('Sorry your name must be longer than two characters.')
		isValid = False

	if isValid == True:
		session['user'] = name
		return redirect('/ninja_gold')
	else:
		return redirect('/')

@app.route('/ninja_gold')
def game():
	if 'user' not in session:
		return redirect('/')
	else:
		if 'gold' not in session:
			session['gold'] = 0
		if 'activities' not in session:
			session['activities'] = []
		return render_template('game.html')

@app.route('/money', methods=['POST'])
def money():
	location = request.form['location']
	if location == 'farm':
		gold = random.randrange(10, 21)
	elif location == 'cave':
		gold = random.randrange(5, 11)
	elif location == 'house':
		gold = random.randrange(10, 16)
	else:
		gold = random.randrange(-50, 51)

	session['gold'] += gold

	if gold > 0:
		pos_neg = 'earned'
		html_class = 'green'
	else:
		pos_neg = 'lost'
		html_class = 'red'

	str = "You {} {} gold from the {}!".format(pos_neg,abs(gold), location)

	msgObj = {
		'message': str,
		'class': html_class,
	}

	session['activities'].insert(0, msgObj)

	return redirect('/ninja_gold')

app.run(debug=True)