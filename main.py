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
		article = mongo.db.articles.find_one({'Titre': request.form['search']})
		return render_template('article.html', article = article)
	return render_template('index.html')
	
@app.route('/<chaine>/')
def connexion_article(chaine):
	article = mongo.db.articles.find_one({'Titre': chaine})
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
	

@app.route('/article/<chaine>/commentaires/')
def ajouterCommentaire():
    newComment = commentaires(chaine, request.form["Auteur_comment"], datetime.datetime.now(),
                              request.form["contenu_commment"])
    if newComment.isValid() == True:
        ajoutComment = mongo.db.commentaires.insert_one(newComment.format)
        return render_template('temp_Conf_soumissionComment.html')  # page à renvoyer
    else:
        return render_template(
            'template_FormArticle.html')  # page à renvoyer   / à modifier pour afficher message d'erreur

    return render_template('template_FormCommentaires.html')  # page à consulter pour récupérer les informations nécessaires


if __name__ == '__main__':
	app.run(debug=True)
