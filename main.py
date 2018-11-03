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

@app.route('/ajouterArticle', methods=['GET', 'POST'])
def ajouterArticle():
    newArticle = {}
    if request.method == 'POST':
        Auteur_article = request.form[
            "Auteur_name"]  # attribut name de l'input (voir formulaire page html 'template_FormArticle.html'
        Titre_article = request.form["titre_article"]
        Mots_cles_article = request.form["Mots_cles_article"]
        Contenu_article = request.form["contenu_article"]
        newArticle = {'Auteur': Auteur_article, 'Titre': Titre_article, 'Mots_cles': Mots_cles_article,
                      'Contenu': Contenu_article}
        ajoutArticle = mongo.db.monuments.insert_one(newArticle)
        return render_template('temp_Conf_soumissionArticle.html')
    return render_template('template_FormArticle.html')

if __name__ == '__main__':
	app.run(debug=True)
