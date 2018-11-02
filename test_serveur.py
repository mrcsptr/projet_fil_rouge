
 
import flask
TPL = flask.render_template # Pour éviter de toujours taper flask.render_template...
 
app = flask.Flask(__name__, template_folder='.')
 
@app.route('/')
def info():
    data = """\
    Bonjour Visiteur
    """
    return TPL("default_html.html", title='Home', data=data)
 
@app.route('/paramurl/<int:number>')
def paramurl(number):
    data = """\
    Vous avez mis  {} dans l'URL.
    """.format(number)
    return TPL("default_html.html", title='ParamUrl', data=data)
 
@app.route('/paramget')
def paramget():
    login = flask.request.args['login']
    data = """\
    Le login entré est {}.
    """.format(login)
    return TPL("default_html.html", title='Paramget', data=data)
 
@app.route('/formulaire')
def formulaire():
    data = """\
    <form action="validate" method="post">
    <input type="text" name="login"/><br/>
    <input type="submit"/>
    </form>
    """
    return TPL("default_html.html", title='Formulaire', data=data)
 
# Récupération des données d'un formulaire, en POST uniquement
# Si les données sont postées en json et non en 
# application/x-www-form-urlencoded ou multipart/form-data 
# utiliser flask.request.get_json()  au lieu
# de flask.request.form
@app.route('/validate', methods=["POST"])
def validate():
    login = flask.request.form['login']
    data = """\
    Le login entré est {}.
    """.format(login)
    return TPL("default_html.html", title='Validate', data=data)
 
 
# Renvoie du json
@app.route('/data_json')
def data_json():
    liste = [1, 2, 3, "toto"]
    dico = {"val1": liste, "val2": "Salut"}
    return flask.jsonify(dico) # Renvoie la chaîne json en gérant correctement l'entête HTTP
 
# Code de retour :
# https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP
@app.route('/forbidden')
def forbidden():
    flask.abort(403)
 
 
@app.route('/redirect_me')
def redirect_me():
    return flask.redirect(flask.url_for('info'))
 
 
print("PATH =====>", app.instance_path)
if __name__ == '__main__':
    #app.config['DEBUG'] = True
    #app.secret_key = 'mysecretkey3*lezneri123445'
    #app.run(host='0.0.0.0', port=5000)
	app.run(debug=True)