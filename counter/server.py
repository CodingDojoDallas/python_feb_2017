from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key= 'secretSquirrels'

@app.route('/')
def index():
    return render_template('index.html', times=session['times'])

@app.route('/count')
def count():
    if 'times' not in session:
        session['times'] = 1
    else :
        session['times'] += 1
    return redirect('/')

@app.route('/clear')
def clear():
    if session['times'] >1 :
        session['times']=1
    return redirect('/')
app.run(debug=True)
