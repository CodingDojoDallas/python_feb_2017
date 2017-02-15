from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'thisissecret'
import random


@app.route('/')
def start():
    if 'totalgold' not in session:
        session['totalgold'] = 0
    if 'result' not in session:
        session['result'] = ' '
    return render_template("main.html")

@app.route('/process_money', methods=['POST'])
def display():
    if request.form['building'] == 'farm':
        num = random.randint(10,20)
        session['totalgold'] += num
        session['result'] += "Earned " + str(num) + " gold from the farm! "
    elif request.form['building'] == 'cave':
        num = random.randint(5,10)
        session['totalgold'] += num
        session['result'] += "Earned " + str(num) + " gold from the cave! "
    elif request.form['building'] == 'house':
        num = random.randint(2,5)
        session['totalgold'] += num
        session['result'] += "Earned " + str(num) + " gold from the house! "
    elif request.form['building'] == 'casino':
        chance = random.randint(1,3)
        if chance == 1:
            num = random.randint(0,51)
            session['totalgold'] += num
            session['result'] += "Entered a casino and won " + str(num) + " gold, yay! "
        elif chance == 2:
            num = random.randint(0,51)
            session['totalgold'] -= num
            session['result'] += "Entered a casino and lost " + str(num) + " gold...Ouch... "
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
