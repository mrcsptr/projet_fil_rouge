from flask import *

app = Flask (__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    recherche = formulaire_recherche_page(request.form)
    if request.method == 'POST':
        return search_results(recherche)

    return render_template('index.html', form=search)


"""@app.route("/se_deconnecter")
def se_deconnecter ():
    session.pop("e_mail", None)
    flash('Vous etes maintenant deconnecte.')
    return redirect(url_for('se_connecter'))"""


if __name__ == '__main__' :
    app.run(debug=True)