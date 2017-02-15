from flask import *
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'thisissecret'
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
mysql = MySQLConnector(app, 'login_register')


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("index.html")

@app.route('/success')
def index():
    query = 'SELECT * FROM users WHERE id = :id'
    values = {'id': session['user_id']}
    user = mysql.query_db(query, values)
    data = {'user':user}
    return render_template("success.html", data=data)

@app.route('/home')
def home():
    query = 'SELECT * FROM users WHERE id = :id'
    values = {'id': session['user_id']}
    user = mysql.query_db(query, values)
    data = {'user':user}
    return render_template('home.html', data=data)


@app.route('/submission', methods=['POST'])
def submission():
    require = 0
    if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['password_confirm']) < 1:
        flash("An input field is empty! Please fill out everything.")
    else:
        require += 1

    if len(request.form['first_name']) < 3 or len(request.form['last_name']) < 3:
        flash("First name and last name must be longer than 2 characters.")
    else:
        require += 1

    if request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("Invalid characters in name field(s).")
    else:
        require += 1

    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long!")
    else:
        require += 1

    if request.form['password'] != request.form['password_confirm'] or request.form['password_confirm'] != request.form['password']:
        flash("Your password and confirm password do not match")
    else:
        require += 1

    if not EMAIL_REGEX.match( request.form['email'] ):
        flash("Invalid Email Address!")
    else:
        require += 1

    if require == 6:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        values = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        user_id = mysql.query_db(query, values)
        session['user_id'] = user_id
        return redirect('/success')
    else:
        flash("Please meet all the requirements for signing up.")
    return redirect('/')

@app.route('/login', methods=['POST'])
def user_home():
    query = "SELECT id, email, first_name, last_name, password FROM users WHERE email = :email"
    data = {
        'email': request.form['email']
    }
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        session['user_id'] = user[0]['id']
        return redirect('/home')
    else:
        flash("Your email and password do not match.")
        return redirect('/')

app.run(debug=True)
