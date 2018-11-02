#main

# coding: utf-8

from flask import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ajouterArticle', methods=['GET', 'POST'])
def ajouterArticle():
	return render_template("template_FormArticle.html")


@app.route('/infos', methods=['GET', 'POST'])
def infos ():
	if request.method == 'POST':
		Auteur = request.form["Auteur"]
		Titre = request.form["Titre"]
		#return "Les infos sont {0} et {1}".format(Auteur , Titre)
		#Exploitation des donnéess...     
	return render_template('temp_Conf_soumissionArticle.html')
	
	
@app.route("/getArticleList", methods=['GET', 'POST'])
def getArticleList():

	# Initialize a employee list
	ArticleList = []
	articleDict = {}
	return render_template("template_FormArticle.html", auteur = request.form["Auteur_name"], titre = request.form["titre_article"])
	# create a instances for filling up employee list
	for i in range(0,1):		
		articleDict = {
		'Auteur_name': auteur, 
		'titre_article': titre }
		ArticleList.append(articleDict)

	# convert to json data
	jsonStr = json.dumps(ArticleList)

	return jsonify(Articles=jsonStr)
	
if __name__ == '__main__':
	app.run(debug=True)