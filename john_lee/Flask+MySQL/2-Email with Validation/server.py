from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'thisissecret'
mysql = MySQLConnector(app,'emaildb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('index.html', all_email=email)

@app.route('/email/<email_id>')
def show(email_id):
    query = "SELECT * FROM email WHERE id = :specific_id"
    data = {'specific_id': email_id}
    email = mysql.query_db(query, data)
    return render_template('index.html', one_email=email[0])

@app.route('/email', methods=['POST'])
def create():
    if not EMAIL_REGEX.match(request.form['emailaddress']):
        flash("Invalid Email Address!")
    else:
        query = "INSERT INTO email (emailaddress, created_at, updated_at) VALUES (:emailaddress, NOW(), NOW())"
        data = {
                 'emailaddress': request.form['emailaddress'],
                 'created_at': request.form['created_at'],
                 'updated_at': request.form['updated_at']
               }
        mysql.query_db(query, data)
        flash("The email you entered, "+request.form['emailaddress']+", is a VALID email address! Thank you!")
    return redirect('/')

app.run(debug=True)
