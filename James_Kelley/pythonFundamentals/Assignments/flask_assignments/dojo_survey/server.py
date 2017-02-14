from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route ('/')

def dojoSurvey():
	return render_template('index.html')

@app.route('/results', methods=['post'])

def results():

	name = request.form['name']
	location = request.form['codingDojo']
	language = request.form['language']
	comment = request.form['comment']


	return render_template('results.html', name= name,
	 location= location, language=language, comment=comment)
	


app.run(debug=True)