# coding: utf-8
# Python 3.6
# Thème Inktober : Construire

import tkinter as tk
from PIL import ImageTk

class App(tk.Tk):

	def __init__(self):
		super().__init__()
		self.geometry("640x320") 

		self.briques = []
		self.img = ImageTk.PhotoImage(file="brique.png")

		for x in range(10): # On créer un espace de 10x10
			briques_y = []
			self.briques.append(briques_y)
			for y in range(10):
				brique = tk.Label(self, bd=0)
				brique.place(x=x*64, y=y*32)
				briques_y.append(brique)

		# Quand une touche est pressée, on appel construire
		self.bind('<KeyPress>', self.construire)
		self.mainloop()

	def construire(self, evenement):
		choix = evenement.char # On récupére la touche pressée dans choix

		if choix in ["0","1","2","3","4","5","6","7","8","9"]:
			# On passe de texte à nombre
			colonne = int(choix)
			self.ajout_brique(colonne)

	def ajout_brique(self, colonne):

		if colonne < 10:
			for ligne in sorted(range(10), reverse=True):
				if not self.briques[colonne][ligne]['image']:
					self.briques[colonne][ligne].config(image=self.img)
					break
App()