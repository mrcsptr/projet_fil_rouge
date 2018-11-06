#main

# coding: utf-8

from flask import *
from flask_pymongo import PyMongo
from article import *
import datetime

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wiki"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		article = mongo.db.articles.find({'Titre': request.form['search']})[0]
		return render_template('article.html', article = article)
	return render_template('index.html')
	
@app.route('/<chaine>/')
def connexion_article(chaine):
	article = mongo.db.articles.find({'Titre': chaine})[0]
	return render_template('article.html', article = article)

@app.route('/ajouterArticle/', methods=['GET', 'POST'])
def ajouterArticle():
	if request.method == 'POST':
		newArticle = article(request.form["titre_article"],request.form["Auteur_name"], datetime.datetime.now(), request.form["contenu_article"], request.form["categorie_article"], request.form["Mots_cles_article"])
		if newArticle.isValid() == True:
			ajoutArticle = mongo.db.articles.insert_one(newArticle.format)
			return render_template('temp_Conf_soumissionArticle.html')
		else:
			return render_template('template_FormArticle.html')
			
	return render_template('template_FormArticle.html')
	
#@app.route('/ajouterCommentaire/', methods=['GET', 'POST'])
#def ajouterCommentaire ():
#	if request.method == 'POST':
#		Auteur_commentaire = request.form["Auteur_comment"]                # attribut name de l'input (voir formulaire page html 'article.html'
#		Contenu_commentaire = request.form["contenu_comment"]
#		# ajouter le contenu du commentaire dans la base de données mongoDB
#		ajoutComment = mongo.db.monuments.update({'auteur': Auteur_commentaire}, {$set:{'Commentaires': Contenu_commentaire}})     # vérifier comment 'auteur' est écrit dans la base de données mongoDB
#		return render_template('temp_Conf_soumissionArticle.html')     # page à retourner
#	return render_template('article.html', monuments = monuments)      # page à consulter pour récupérer les informations nécessaires

if __name__ == '__main__':
	app.run(debug=True)
