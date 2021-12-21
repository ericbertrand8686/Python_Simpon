from tkinter import Tk, Canvas

class tableauAffichage:
    def __init__(self, window):
        window.geometry("750x505")
        window.title("Le jeu du Morpion - Stéphane Pasquet (mathweb.fr)")
        # label = Label(window, text="Le jeu du Morpion (OXO)", font=("Helvetica", 20)).place(x=190,y=1)
        
        self.game = Canvas(window, width = 405, height = 405, bg = "white")        

if __name__ == '__main__':    
    root = Tk()
    tableauAffichage(root)