from flask import Flask, render_template, request, redirect,session, flash
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
    if len(request.form['name']) < 1 or len(request.form['comment']) > 120:
        if len(request.form['name']) < 1:
            flash("Name cannot be empty!")
        if len(request.form['comment']) > 120:
            flash("Character limit in comment exceeds 120 charcters!")
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/goback')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
