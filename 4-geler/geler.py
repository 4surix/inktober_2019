# Python 3.6
# Thème Inktober : Geler

import tkinter as tk
from PIL import ImageTk

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.température = 0
        self.chemin = "imgs_bulle/bulle_%s.png"

        self.img = ImageTk.PhotoImage(file= self.chemin % self.température)

        self.bulle = tk.Label(self, image= self.img)
        self.bulle.grid()

        self.after(1000 * 10, self.refroidissement)

        self.mainloop()

    def refroidissement(self):

        if self.température > -15:

            self.img = ImageTk.PhotoImage(file= self.chemin % self.température)
            self.bulle.config(image= self.img)
            # On baisse la température 
            self.température -= 1
            # On re-appel refroidissement dans 1 seconde
            self.after(1000 * 1, self.refroidissement)

App()

