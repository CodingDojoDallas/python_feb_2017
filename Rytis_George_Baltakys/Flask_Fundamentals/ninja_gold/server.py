from flask import *
import random, time
app = Flask(__name__)
app.secret_key = 'alskdjsrop23ws8fjcaffwf'

@app.route('/')
def root():

	# get or initialize session variables
	if 'gold' not in session:
		session['gold'] = 0
		session['win'] = 0
		session['where'] = ''
		session['output'] = []

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

	# reset game
	if 'reset' in request.form:
		session.clear()
		return redirect('/')

	if 'farm' in request.form:
			session['win'] = random.randrange(10, 21)
			session['where'] = 'farm'
	if 'cave' in request.form:
			session['win'] = random.randrange(5, 11)
			session['where'] = 'cave'
	if 'house' in request.form:
			session['win'] = random.randrange(2, 6)
			session['where'] = 'house'
	if 'casino' in request.form:
			session['win'] = random.randrange(-50, 51)
			session['where'] = 'casino'

	session['gold'] += session['win']

	activity = ''
	if session['win'] > 0:
		activity += '<span class="gold">Eearned ' + str(session['win']) + ' gold from the ' + str(session['where'])
	else:
		activity += '<span class="loss">Lost ' + str(abs(session['win'])) + ' gold from the ' + str(session['where']) + '. Ouch..'
	activity += '! (' + time.asctime( time.localtime(time.time()) ) + ')</span><br>'

	session['output'].insert(0, activity)

	return redirect('/')

app.run(debug=True)