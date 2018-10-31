#main

# coding: utf-8

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	return "bienvenue sur le wiki !"
	
	
@app.route('/<chaine>/')
def connexion_article(chaine):
	return str(chaine)


if __name__ == '__main__':
	app.run(debug=True)
