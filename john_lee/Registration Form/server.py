from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
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
    require = 0
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash("An input field is empty! Please fill out everything.")
    else:
        require += 1

    if request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("Names cannot include numbers.")
    else:
        require += 1

    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long!")
    else:
        require += 1

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        require += 1

    if request.form['password'] != request.form['confirm_password'] or request.form['confirm_password'] != request.form['password']:
        flash("Your password and confirm password do not match")
    else:
        require += 1

    if(require == 5):
        flash("Thank you for signing up!")
    else:
        flash("Please meet all the requirements for signing up.")

    return redirect('/')


app.run(debug=True)
