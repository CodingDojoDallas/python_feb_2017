from flask import *
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'secrets'

mysql = MySQLConnector(app, 'the_wall_123')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW());"
	values = {
		'name': request.form['name'],
		'email': request.form['email'],
		'password': bcrypt.generate_password_hash(request.form['password']),
	}
	user_id = mysql.query_db(query, values)
	session['user_id'] = user_id
	return redirect('/wall')

@app.route('/sessions', methods=['POST'])
def login_user():
	query = 'SELECT * FROM users WHERE email = :email;'
	values = { 'email': request.form['email'] }
	user = mysql.query_db(query, values)
	if len(user) > 0 and bcrypt.check_password_hash(user[0]['password'], request.form['password']):
		session['user_id'] = user[0]['id']
		return redirect('/wall')
	else:
		flash('Invalid credentials')
		return redirect('/')

@app.route('/wall')
def wall():
	query = 'SELECT users.name, users.email FROM users WHERE id = :id;'
	values = { 'id': session['user_id'] }
	current_user = mysql.query_db(query, values)[0]
	query2 = "select messages.id as message_id, messages.message, messages.created_at as message_date, users.name as message_user, comments.id as comment_id, comments.comment, comments.created_at as comment_date, comments_users.name as comment_user from users join messages on messages.user_id = users.id left join comments on comments.message_id = messages.id left join users as comments_users on comments_users.id = comments.user_id;"
	messages = mysql.query_db(query2)

	new_messages = []
	dump = []
	for message in messages:
		if message['message_id'] not in dump:
			dump.append(message['message_id'])
			msg_obj = {}
			msg_obj['message_id'] = message['message_id']
			msg_obj['message'] = message['message']
			msg_obj['message_user'] = message['message_user']
			msg_obj['message_date'] = message['message_date']
			msg_obj['comments'] = []
			new_messages.append(msg_obj)
		if message['comment'] != None:
			comment_obj = {}
			comment_obj['comment_id'] = message['comment_id']
			comment_obj['comment'] = message['comment']
			comment_obj['comment_user'] = message['comment_user']
			comment_obj['comment_date'] = message['comment_date']
			new_messages[-1]['comments'].append(comment_obj)

	data = {
		'current_user': current_user,
		'messages': new_messages,
	}
	return render_template('wall.html', data=data)

@app.route('/messages', methods=['POST'])
def create_message():
	query = 'INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW());'
	values = {
		'message': request.form['message'],
		'user_id': session['user_id'],
	}
	mysql.query_db(query, values)
	return redirect('/wall')

@app.route("/comments/<id>", methods=['POST'])
def create_comment(id):
	query = "INSERT INTO comments (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW());"
	values = {
		'comment': request.form['comment'],
		'message_id': id,
		'user_id': session['user_id'],
	}
	mysql.query_db(query, values)
	return redirect('/wall')

app.run(debug=True)
