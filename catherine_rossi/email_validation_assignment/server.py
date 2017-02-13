from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends_db')

@app.route('/') #homepage
def index():
    return render_template('index.html')

@app.route("/emails", methods=["POST"]) 
def insert():
    #validating emails using html5
    query = "INSERT INTO emails (email) VALUES (:email)"   
    data ={
            "email": request.form["email_address"]
          }
    mysql.query_db(query, data)
    return redirect('/sucess')

@app.route("/sucess")
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query) 
    return render_template('sucess.html', all_emails=emails) 

app.run(debug=True)
