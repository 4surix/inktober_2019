import random

caractères = ' abcde fghij klmnop qrstuv wxyz'
# Nombre de caractéres
nbr_caractères = len(caractères)-1

def phrase_debile_aléatoire():
    phrase = ""
    taille_phrase = 10
    # Augmentation aléatoire de la taille entre 0 et 10 de la phrase
    taille_phrase += random.randint(0, 10)
    # Boucle qui tourne autant de fois que la taille de la phrase
    for _ in range(taille_phrase):
        # Position aléatoire
        position = random.randint(0, nbr_caractères)
        # Ajout du caractère dans la phrase
        phrase += caractères[position] 

    return phrase

def analyse_phrase_utilisateur(phrase):
    # On passe tout les caractères de la phrase en minuscule
    phrase = phrase.lower()

    if 'je ne suis pas stupide' in phrase:
        return "Si vous êtes stupide."

    elif 'je suis stupide' in phrase:
        return "Oui vous êtes stupide."

    elif 'tu es stupide' in phrase:
        return "Non je ne suis pas stupide, c'est vous qui l'êtes !"

    elif 'stupide' in phrase:
        return "Qu'est ce que stupide ? Cela se mange ?"

    else:
        return phrase_debile_aléatoire()

# On créer la 1er phrase à afficher
phrase_robot = phrase_debile_aléatoire()

while True:
    print('Robot: ' + phrase_robot)

    phrase_utilisateur = input('Vous: ')

    # On définie la phrase du robot en fonction de ce que
    # la phrase de l'utilisateur contient
    phrase_robot = analyse_phrase_utilisateur(phrase_utilisateur)