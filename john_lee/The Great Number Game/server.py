from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisissecret'
import random

@app.route('/')
def index():
  return render_template("index.html")

number = random.randint(1,101)

@app.route('/', methods=['POST'])
def display():
    print "got input"
    guess = int(request.form['guess'])
    session['gamestate']=''
    if guess > number:
        print ("Lower...")
        session['gamestate'] = "Lower"
    elif guess < number:
        print("Higher...")
        session['gamestate'] = "Higher"
    else:
        print("You guessed it!")
        session['gamestate'] = "You Guessed It"
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
