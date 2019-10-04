# coding: utf-8
# Python 3.6
# Thème Inktober : Appât

import random

txt_erreur_capturée = "   Erreur '%s' capturée ! "
txt_nouv_erreur = "   Nouvelle erreur '%s' !"

erreurs_capturées = {}

def suite_nombre(début, fin):

    suite = []
    nbr = début

    while nbr <= fin:
        suite.append(nbr)
        nbr += 1

    return suite

def creer_erreur():
    # num vaut un nombre aléatoire entre 0 et 100
    num = random.randint(0, 100)
    
    # Plus la suite de nombre est petite
    # plus l'erreur est rare !
    if num == 0:
        5/0
    elif num in suite_nombre(1, 5):
        "a" - "b"
    elif num in suite_nombre(6, 15):
        print(pomme)
    elif num in suite_nombre(16, 30):
        open("defghjhgfdsqsdfgh.txt")
    elif num in suite_nombre(31, 100):
        "pouf"()

def lancer_appât():

    try: creer_erreur()
    except Exception as erreur_:
        #On récupére le nom de l'erreur
        erreur = erreur_.__class__.__name__

        if erreur not in erreurs_capturées:
            print(txt_nouv_erreur % erreur)
            erreurs_capturées[erreur] = 1
        else:
            print(txt_erreur_capturée % erreur)
            erreurs_capturées[erreur] += 1

while True:
    print("\nCombien de fois voulez vous lancé l'appât ?")
    nbr_lancés = int(input())

    print("\nLancement d'appât: ")

    for _ in range(nbr_lancés):
        lancer_appât()

    print('\nSac: ')

    for erreur, nbr_attrapée in erreurs_capturées.items():
        print('    %s erreur(s) %s' % (nbr_attrapée, erreur)) 