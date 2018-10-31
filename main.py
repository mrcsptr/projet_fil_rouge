#main

# coding: utf-8

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
	return "courage les gens, merci  !"


if __name__ == '__main__':
	app.run(debug=True)
