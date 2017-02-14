from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def Hello_There():
	return render_template('index.html')

@app.route('/ninjas')

def Ninjas():
	return render_template('ninjas.html')

@app.route('/dojos/new')

def Dojos_New():
	return render_template('dojos.html')


app.run(debug=True)