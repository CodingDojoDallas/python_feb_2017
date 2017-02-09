from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'thisissecret'

@app.route('/')
def index():
    return render_template("ninja.html")

@app.route('/<vararg>')
def handler_function(vararg):
    if vararg == "blue":
        return render_template("blue.html",vararg=vararg)
    if vararg == "orange":
        return render_template("orange.html",vararg=vararg)
    if vararg == "red":
        return render_template("red.html",vararg=vararg)
    if vararg == "purple":
        return render_template("purple.html",vararg=vararg)
    else:
        return render_template("april.html",vararg=vararg)
        
app.run(debug=True)
