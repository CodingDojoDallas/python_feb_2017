from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'thisissecret'

def sessioner():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1

@app.route('/')
def count():
    sessioner()
    return render_template('index.html')

app.run(debug=True)
