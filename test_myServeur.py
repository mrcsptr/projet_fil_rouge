# coding: utf-8

from flask import *
 
app = Flask(__name__)

@app.route('/')
def info():
    data = """\
    Bonjour Visiteur
    """
    return render_template("template_FormArticle.html", title='Home', data=data)

@app.route('/article', methods=['GET', 'POST'])
def auteur():
	if request.method == 'POST':
		auteur = request.form["Auteur_name"]
		return "L'auteur entré est {auteur}.".format(auteur)
	return render_template("template_FormArticle.html")
	
@app.route("/getArticleList", methods=['GET', 'POST'])
def getArticleList():

	# Initialize a employee list
	ArticleList = []
	articleDict = {}
	#if request.method == 'POST':
	#	auteur = request.form["Auteur_name"]
	#	titre = request.form["titre_article"]

	# create a instances for filling up employee list
	for i in range(0,2):
	
		if request.method == 'POST':
			articleDict = {
			'Auteur_name': request.form["Auteur_name"],
			'titre_article': request.form["titre_article"] }
			return render_template("template_FormArticle.html")
		ArticleList.append(articleDict)

	# convert to json data
	jsonStr = json.dumps(ArticleList)

	return jsonify(Articles=jsonStr)
	
if __name__ == '__main__':
	app.run(debug=True)