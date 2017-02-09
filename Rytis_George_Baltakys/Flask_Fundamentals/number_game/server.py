from flask import Flask, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = 'alskdjrop23w8fjawf'

@app.route('/')
def root():
	# reset game
	if 'button' in request.args:
		if request.args['button'] == 'Play again!':
			session.clear()

	hint = ''
	win = False
	guess = None

	if 'num' not in session:
		session['num'] = random.randrange(0, 101)
	if 'guess' in request.args:
		guess = int(request.args['guess'])
		if session['num'] == guess:
			hint = 'You guessed it!'
			win = True
		elif session['num'] < guess:
			hint = 'Too high'
		else:
			hint = 'Too low'
	else:
		hint = 'Take a guess!'
		
	return render_template('index.html', hint=hint, win=win, guess=guess)

app.run(debug=True)