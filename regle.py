# -*-coding:utf-8-*
from tkinter import *

def lesRegles():

    lesRegles = "L'ordinateur choisira un mot au hasard. Vous allez tenter de \n" \
                "trouver les lettres composant le mot. À chaque coup,\n" \
                " vous saisissez une lettre. Si la lettre figure dans\n " \
                "le mot,l'ordinateur affiche le mot avec les lettres\n" \
                "déjà trouvées. Celles qui ne le sont pas encore sont\n" \
                " remplacées par des étoiles (*). Vous avez 8 chances.\n" \
                " Au delà, vous avez perdu.Le jeu peut enregister votre\n" \
                " score, votre nom sera l’identifiant. Votre score sera\n" \
                "le nombre de coup restant une fois le not trouvées"

    def fermerRegle():
        fenetreRegle.destroy()

    fenetreRegle=Tk()

    fenetreRegle.title("Fandr's app")
    fenetreRegle.geometry("720x400")
    fenetreRegle.minsize(700,500)
    fenetreRegle.maxsize(720,400)
    fenetreRegle.iconbitmap("icon.ico")
    fenetreRegle.config(background='#195c85')

    #Bloc regle
    frameRegle = Frame(fenetreRegle,bg='#195c85',relief=SUNKEN,bd=0,highlightthickness=0)
    lablelRegle= Label(frameRegle,text=lesRegles,font=("Arial",16,'italic'),bg='#195c85')
    lablelRegle.pack(expand=True)
    frameRegle.pack(expand=True)

    #Bouton fermer
    boutonFermer = Button(fenetreRegle, text="Fermer", command=fermerRegle, bg='#dbdcff', font=('Arial', 10))
    boutonFermer.place(x=325, y=390)


    fenetreRegle.mainloop()