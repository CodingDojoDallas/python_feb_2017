from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'itcanbeanythingyouwant'


@app.route("/") #methods=['GET']
def index():
	# print session['name']
	return render_template('index.html')

@app.route("/processingForm", methods=['POST'])
def form():
	name = request.form['name']
	#session is a dictionary aka object
	session['name'] = []
	session['name'].append(name)
	return redirect('/')


app.run(debug=True)
