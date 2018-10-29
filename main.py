#main

# coding: utf-8

from flask import *

app = Flask(__name__)


def index():
	return "courage les gens !"


if __name__ == '__main__':
	app.run(debug=True)