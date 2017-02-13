from flask import *
import random
app = Flask(__name__)
app.secret_key = 'secretSquirrel'

@app.route('/')
def index():
    session['number']= random.randrange(1,101)
    if 'guess' not in session:
        session['guess']= request.form['guess']
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if session['guess'] !=session['number']:
        session['result']="You win"
        return redirect('/')
    elif session['guess'] == session['number']:
        print "working"
        session['result']="Guess again"
        return redirect('/')


app.run(debug=True)
