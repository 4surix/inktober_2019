# coding: utf-8
# Python 3.6
# Thème Inktober : Husky

import tkinter as tk
from PIL import Image, ImageTk

class yeux:
	def __init__(self):
		self.forme = ""
		self.couleur = ""

class animal:
	def __init__(self):
		self.taille = 0
		self.poids = 0
		self.tête = ""
		self.caractère = "" 
		self.yeux = yeux()
		self.image = ""

class chien(animal):
	def __init__(self):
		super().__init__()

		self.pattes = 4
		self.queue = ""
		self.oreilles = ""
		self.poil = ""

husky = chien()

husky.taille = 50 ;  husky.poids = 25 ;  husky.tête = "ronde"
husky.poil = "Doux, lisse et de longueur moyenne"
husky.oreilles = "Triangulaires, dressées, l'extrémité arrondie pointe vers le ciel"
husky.queue = "Moyenne, touffue, légèrement relevée en forme de faucille"
husky.caractère = "Doux, gentil, sociable, sportif et têtu"
husky.yeux.forme = "amande"
husky.yeux.couleur = "noir/marron/bleu/vairon"
husky.image = "husky.jpg"

class presentation(tk.Tk):

	def __init__(self, animal):
		super().__init__()
		self.geometry("800x350") 

		self.x = 25
		self.y = 25

		self.ajoute_label("Taille : "+str(animal.taille)+" cm")
		self.ajoute_label("Poids : "+str(animal.poids)+" kg")
		self.ajoute_label("Oreilles : "+animal.oreilles)
		self.ajoute_label("Queue : "+animal.queue)
		self.ajoute_label("Poil : "+animal.poil)
		self.ajoute_label("Yeux : "+animal.yeux.forme+" | "+animal.yeux.couleur)
		self.ajoute_label("Caractère : "+animal.caractère)

		image = Image.open(animal.image)
		image = image.resize((300, 300))
		self.img = ImageTk.PhotoImage(image)

		image = tk.Label(self, image=self.img)
		image.place(x= 475, y= 25)

		self.mainloop()

	def ajoute_label(self, texte):
		indication = tk.Label(self, text= texte)
		indication.place(x= self.x, y= self.y)
		self.y += 25
		return indication

presentation(husky)