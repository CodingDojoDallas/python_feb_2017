from flask import *
app = Flask(__name__)
app.secret_key = 'alskdjdrop23w8fjawf'

@app.route('/')
def root():
	return render_template('index.html')

@app.route('/<color>')
def process(color):

	ninja = ''
	
	if color == 'blue':
		ninja = 'leonardo'
	elif color == 'orange':
		ninja = 'michelangelo'
	elif color == 'red':
		ninja = 'raphael'
	elif color == 'purple':
		ninja = 'donatello'
	else:
		ninja = 'notapril'

	return render_template('ninja.html', ninja=ninja)


app.run(debug=True)