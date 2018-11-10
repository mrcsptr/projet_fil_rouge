#main

# coding: utf-8

from flask import *
from flask_pymongo import PyMongo
from article import *
import datetime
from commentaire import *
import re
from flask import session

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wiki"
mongo = PyMongo(app)
app.secret_key = 'my secret key'  # clé secrète et unique à fixer pour pouvoir 
# utiliser la messagerie flash. Cette messagerie utilise un mécanisme de stockage 
# de la session pour contenir les messages entre les demandes. Il disparaîtra la 
# prochaine fois qu'on arrive à la page automatiquement.

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		article = mongo.db.articles.find_one({'Titre': request.form['search']})
		return redirect(url_for('connexion_article', chaine = article['Titre']))
	return render_template('index.html')
	
@app.route('/seConnecter/', methods=['GET', 'POST'])
def seConnecter():
	if request.method == 'POST':
		pseudo = request.form["pseudo"]        # récupération du pseudo
		if pseudo in session:                  # si le pseudo était déjà enrégistré
			return render_template('espacePerso.html', pseudo=session[pseudo])   # on renvoit la page perso de l'utilisateur
		else:
			session[pseudo] = pseudo           # si le pseudo n'était pas encore enrégistré
			return render_template('NewespacePerso.html', pseudo=session[pseudo])    # on renvoit la page perso du nouvel utilisateur avec le message bienvenu
	return render_template('seConnecter.html')
	
@app.route('/<chaine>/')
def connexion_article(chaine):
	article = mongo.db.articles.find_one({'Titre': chaine})
	return render_template('article.html', article = article)

@app.route('/ajouterArticle/', methods=['GET', 'POST'])
def ajouterArticle():
	if request.method == 'POST':
		newArticle = article(request.form["titre_article"],request.form["Auteur_name"], datetime.datetime.now(), 
			request.form["contenu_article"], request.form["categorie_article"], request.form["Mots_cles_article"])
		if newArticle.isValid():
			ajoutArticle = mongo.db.articles.insert_one(newArticle.format)
			return render_template('temp_Conf_soumissionArticle.html')
		else:
			return render_template('template_FormArticle.html')
			
	return render_template('template_FormArticle.html')
	

@app.route('/<chaine>/commentaires/', methods=['GET', 'POST'])
def ajouterCommentaire(chaine):
	if request.method == 'POST':
		newComment = commentaires(chaine, request.form["Auteur_comment"], datetime.datetime.now(),
                              request.form["contenu_comment"])   # création d'un nouvel objet commentaire avec les information saisies par l'utilisateur
		if newComment.contenu_isValid():
			ajoutComment = mongo.db.commentaires.insert_one(newComment.format)    # on rajoute les nouvelles informations saisies dans la base de données commentaires
			return render_template('temp_Conf_soumissionComment.html')  # on renvoit la page de confirmation de soumission du commentaire.
		else:
			return render_template(
           'template_FormArticle.html')  # on renvoit la page de l'article # à modifier...
	
	comment = mongo.db.commentaires.find({'Article': chaine})   # on récupère la liste de tous les commentaires de l'article.
	return render_template('template_FormCommentaires.html', comment = comment)  # page à consulter pour récupérer les informations nécessaires


if __name__ == '__main__':
	app.run(debug=True)
