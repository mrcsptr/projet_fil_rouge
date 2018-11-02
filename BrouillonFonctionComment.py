# coding: utf-8
import os
import re

def controlAuto():
    result = 0
    lower_mots_interdit = ["batârd", "bitch", "biatch", "con", "connasse", "couillon", "enfoiré", "fdp", "crétin",
                           "idiot"]
    mots_interdit = [elt.upper() for elt in lower_mots_interdit]
    cap_mots_interdit = [elt.capitalize() for elt in lower_mots_interdit]
    mots_interdit.extend(cap_mots_interdit)
    mots_interdit.extend(lower_mots_interdit)
    print (mots_interdit)

    for elt in mots_interdit:
        for mot in contenu_comment.split():
            if re.search(elt, mot) is None:
                x = 0
            else:
                x = 1
            result += x
    print (result)
    if result == 0:
        return "OK"
    else:
        return "KO"

if __name__=='__main__':
    titre_article = "à la belle étoile! "
    URL_article = "www.monWiki.io/article1"
    auteur_comment = "Fredia"
    contenu_comment = "Je trouve cet article super. CRÉTIN IDIOT Batârd Bitch fdp"


    y = controlAuto()
    print (y)
