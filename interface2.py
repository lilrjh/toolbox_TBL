import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def afficher_page_boutons():
    cadre_accueil.pack_forget()
    cadre_boutons.pack()
def afficher_technique_de_chiffrement():
    cadre_technique.pack_forget()
    cadre_technique.pack()

def bouton1_clic():
    label.config(text="Bouton 1 cliqué")

def bouton2_clic():
    label.config(text="Bouton 2 cliqué")

def bouton3_clic():
    label.config(text="Bouton 3 cliqué")

def bouton4_clic():
    label.config(text="Bouton 4 cliqué")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface avec Image de Fond")

# Charger l'image
image_fond = Image.open("C:/Users/lilia/Pictures/crypto.webp")   # Remplace le chemin par le chemin de ton image
image_fond = image_fond.resize((800, 600), Image.ANTIALIAS)  # Ajuster la taille de l'image si nécessaire
photo_fond = ImageTk.PhotoImage(image_fond)

# Créer un widget Canvas pour afficher l'image de fond
canvas = tk.Canvas(fenetre, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.create_image(0, 0, image=photo_fond, anchor=tk.NW)

# Cadre pour la page d'accueil
cadre_accueil = tk.Frame(canvas)
cadre_accueil.pack(pady=300)

# Boutons sur la page d'accueil
accueil_bouton1 = tk.Button(cadre_accueil, text="chiffrement d'un pdf", command=afficher_technique_de_chiffrement)
accueil_bouton1.pack(side=tk.LEFT, padx=10)
accueil_bouton2 = tk.Button(cadre_accueil, text="chiffrement d'un dossier", command=afficher_page_boutons)
accueil_bouton2.pack(side=tk.LEFT, padx=10)
accueil_bouton3 = tk.Button(cadre_accueil, text="chiffrement d'une video", command=afficher_page_boutons)
accueil_bouton3.pack(side=tk.LEFT, padx=10)
accueil_bouton4 = tk.Button(cadre_accueil, text="chiffrement d'une photo", command=afficher_page_boutons)
accueil_bouton4.pack(side=tk.LEFT, padx=10)
accueil_bouton5 = tk.Button(cadre_accueil, text="chiffrement d'un word", command=afficher_page_boutons)
accueil_bouton5.pack(side=tk.LEFT, padx=10)

cadre_technique=tk.Frame(canvas)
technique_de_chiffrement_symetrique=tk.Button(cadre_technique,texte="chiffrement symétrique",command=afficher_page_boutons)

cadre_boutons = tk.Frame(canvas)
# Création des boutons sur la deuxième page
bouton1 = tk.Button(cadre_boutons, text="Bouton 1", command=bouton1_clic)
bouton2 = tk.Button(cadre_boutons, text="Bouton 2", command=bouton2_clic)
bouton3 = tk.Button(cadre_boutons, text="Bouton 3", command=bouton3_clic)
bouton4 = tk.Button(cadre_boutons, text="Bouton 4", command=bouton4_clic)

# Création d'une étiquette pour afficher les messages
label = tk.Label(cadre_boutons, text="Cliquez sur un bouton")

# Placement des éléments dans le cadre des boutons
bouton1.pack(pady=10)
bouton2.pack(pady=10)
bouton3.pack(pady=10)
bouton4.pack(pady=10)
label.pack(pady=20)

# Boucle principale de la fenêtre
fenetre.mainloop()
