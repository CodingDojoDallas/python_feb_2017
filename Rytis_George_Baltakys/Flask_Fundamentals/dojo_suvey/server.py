from flask import *
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

	formValid = True

	if len(name) == 0 or len(comment) == 0:
		formValid = False
		flash('Please fill in all text fields')
	if len(comment) > 120:
		formValid = False
		flash('Please keep your comments under 120 characters')

	if not formValid:
		return redirect('/')

	session['name'] = name

	return render_template('user.html', name=name, dojo=dojo, language=language, comment=comment)


app.run(debug=True)