from flask import Flask, render_template, url_for, request
global count
count=0
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
@app.route('/room',  methods=['GET', 'POST'])
def room():
	counter=0
	print(request.method)
	if request.method == 'POST':
		if request.form.get('-') == '-':
			counter=counter-1
			print("Encrypted")
			return render_template("room.html",counter=counter)
		elif  request.form.get('+') == '+':
			counter=counter+1
			print("Decrypted")
			return render_template("room.html",counter=counter)
		# preturn render_template("room.html",counter)
	elif request.method == 'GET':
		# return render_template("index.html")
		print("No Post Back Call")
	return render_template("room.html",post=counter)
@app.route('/rm')
def rm():
	return render_template('rm.html')
if __name__ == '__main__':
    app.run(debug=True)
