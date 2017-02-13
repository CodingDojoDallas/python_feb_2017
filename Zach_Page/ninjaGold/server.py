from flask import Flask, request, render_template, redirect, session
import random

app=Flask(__name__)
app.secret_key='anothersecret'

@app.route('/')
def index():
    if 'gold'  not in session:
        session['gold']=0
    if 'activities' not in session:
        session['activities']= []
    return render_template('index.html')

@app.route('/processmoney', methods=['GET','POST'])
def procMoney():
    data = request.form
    print data
    if 'farm' in data:
        gold = random.randrange(10,21)
        session['gold']+= gold
        session['activities'].insert(0, ("Earned {} gold from the farm.").format(gold))
        print session['activities']
    if 'cave' in data:
        gold = random.randrange(5,11)
        session['gold']+= gold
        session['activities'].insert(0, ("Earned {} gold from the cave.").format(session['gold']))
        print session['activities']
    if 'house' in data:
        gold = random.randrange(2,6)
        session['gold']+= gold
        session['activities'].insert(0, ("Earned {} gold from the house.").format(session['gold']))
        print session['activities']
    if 'casino' in data:
        gold = random.randrange(-50,50)
        session['gold']+= gold
        session['activities'].insert(0, ("Earned {} gold from the casino.").format(session['gold']))
        print session['activities']
    if 'clear' in data:
        session['activities'] = []
        session['gold'] = 0

    return redirect('/')


app.run(debug=True)
