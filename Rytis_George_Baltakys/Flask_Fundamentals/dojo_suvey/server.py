from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'alskdjrop23w8fjawf'

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def process():
	name = request.form['name']
	dojo = request.form['dojo']
	language = request.form['language']
	comment = request.form['comment']

	session['name'] = name

	return render_template('user.html', name=name, dojo=dojo, language=language, comment=comment)


app.run(debug=True)