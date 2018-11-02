#main

# coding: utf-8

from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wiki"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		monuments = mongo.db.monuments.find({'INSEE': request.form['search']})
		return render_template('article.html', monuments = monuments)
	return render_template('index.html')
	
@app.route('/<chaine>/')
def connexion_article(chaine):
	monuments = mongo.db.monuments.find({'INSEE': chaine})
	return render_template('article.html', monuments = monuments)


if __name__ == '__main__':
	app.run(debug=True)
