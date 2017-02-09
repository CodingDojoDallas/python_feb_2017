from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'alskdjrop23w8fjawf'

@app.route('/', methods=['POST', 'GET'])
def root():
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1

	if 'ninja' in request.form:
		session['count'] += 1
	elif 'hacker' in request.form:
		session['count'] = 0

	return render_template('index.html', count=session['count'])

app.run(debug=True)