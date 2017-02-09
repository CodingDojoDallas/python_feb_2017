from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result' , methods = ['POST'])
def result():
    data = {
        "location": request.form["location"],
        "favorite_language": request.form["favorite_language"],
        "comment": request.form["comment"],
        "name": request.form["name"]
    }
    return render_template('result.html', data=data)

app.run(debug = True)
