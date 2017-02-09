from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results')
def results():
    return render_template("results.html")

@app.route('/results', methods=['POST'])
def info():
   print "Got Post Info"
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['comment'] = request.form['comment']
   return redirect('/results')

@app.route('/show')
def show_user():
  return render_template('return.html')

app.run(debug=True)
