# coding: utf-8
# Python 3.6
# Thème Inktober : Enchantée
enchantations = {} # Dictionnaire

def analyse_texte(texte):

    for langue in texte.split(';'):
        langue, phrase = langue.split(': ')
        enchantations[langue] = phrase

    return enchantations

f = open("enchantations.txt", encoding="utf-8")
contenue_fichier = f.read()
f.close()
texte = contenue_fichier.replace("\n", "")
analyse_texte(texte)

while True:
    choix_langue = input()
    if choix_langue in enchantations:
        print(enchantations[choix_langue])
    else:
    	print("Cette langue n'existe pas !" \
            + "\nListe des langages :"  \
            + "\n    " + ", ".join(list(enchantations.keys())))