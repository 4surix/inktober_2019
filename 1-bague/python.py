# coding: utf-8


class Bague:

    def __init__(self):
        print("Comment vous appelez-vous ?")
        self.pseudo = input()
        print("Quel forme voulez-vous pour le corp de la bague ?")
        self.corps_de_bague_forme = input()
        print("Quel matériau voulez-vous pour le corp de la bague ?")
        self.corps_de_bague_matériau = input()
        print("Quel pierre précieuse voulez-vous au sommet de la bague ?")
        self.pierre_précieuse = input()
        print("Quel nom voulez-vous donner à votre bague ?")
        self.nom = input()
        print("Combien voulez-vous qu'elle coûte ?")
        self.prix = input()

    def __str__(self):
        return f"{self.nom} | {self.prix}€\n" \
               + "Description:" \
               + f"\n   Magnifique bague fait en {self.corps_de_bague_matériau}, " \
               + f"d'une belle forme {self.corps_de_bague_forme}, " \
               + f"avec par dessus une sublime pierre appelée {self.pierre_précieuse}." \
               + f"\n   Fabriquée par {self.pseudo}"


print("Bienvenue à votre atelier de création de bague !\n")
nouvelle_bague = Bague()
print(nouvelle_bague)
