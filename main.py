# -*-coding:utf-8-*
import os
import sys
from tkinter import *
from fonctions import *
from regle import *

import pickle


#Charger les donnees(nom et score)
with open("donneJoueur","rb") as fic:
    pickeo=pickle.Unpickler(fic)
    donneeJoueur=pickeo.load()

texte1 = ""
liste=[]
essai=8

def enregistrerNom():
    global score
    global texte1
    global motHasard
    global nom
    nom=inputNom.get()
    if nom == "":
        labelNom['text'] = ""
        labelNom['fg'] = 'red'
        labelNom['text'] += "Veuillez ecrire un nom valide"
    else:
        if nom in donneeJoueur.keys():
            score = donneeJoueur[nom]
        else:
            score = 0
            donneeJoueur.update({nom: score})
        labelTexte1['text'] = "Vous etes {} / Votre scrore: {}".format(nom, score) + "\nVous devez trouver le mot:"+("*"*len(motHasard))+"\nVous avez 8 essaies"
        labelNom.destroy()
        inputNom.destroy()
        boutonNom.destroy()
        labelTexte1.grid(row=0,column=0)
        boutonOk.grid(row=2,column=0)
        frameAffichageJeu.place(x=420, y=150)

def ok():
    global essai
    boutonOk.destroy()
    inputLettre.grid(row=1, column=0)
    boutonValiderLettre.grid(row=2, column=0)
    essai-=1


def validerLettre():
    global score
    global nom
    global liste
    global essai
    global motHasard
    inputLettre.grid(row=1, column=0)
    boutonValiderLettre['text'] = "Valider"
    lettreJoueur = inputLettre.get()
    inputLettre.delete(0, len(lettreJoueur))
    if lettreJoueur == "" or not lettreJoueur.isalpha() or len(lettreJoueur)!=1:
        labelAvertissement['text'] = "Attention, veuillez \nentrer une lettre valide"
        labelAvertissement.grid(row=3, column=0)
    elif lettreJoueur in liste:
        labelAvertissement['text'] = "Attention, cette \nlettre a deja été trouvé"
        labelAvertissement.grid(row=3, column=0)
    else:
        labelAvertissement['text'] = ""
        if essai>0:
            if lettreJoueur in motHasard:
                essai+=1
                liste.append(lettreJoueur)
            motAffiche = afficherMot(motHasard, liste)
            labelTexte1['fg'] ='black'
            labelTexte1['text']="Le mot a trouver:  {}\nil vous reste {} essaies".format(motAffiche,essai)

            if motAffiche==motHasard:
                score += essai
                inputLettre.destroy()
                boutonValiderLettre.destroy()
                labelTexte1['fg'] = 'black'
                labelTexte1['text']="Felicitation ! vous avez trouvé le mot,\n vu qu'il vous reste {} essaies,\n vous avez obtenu le score de {}".format(essai,score)

                donneeJoueur.update({nom:score})
                with open("donneJoueur","wb") as fic:
                    pickleo=pickle.Pickler(fic)
                    pickleo.dump(donneeJoueur)

        if essai==0:
            labelTexte1.destroy()
            inputLettre.destroy()
            boutonValiderLettre.destroy()
            labelRejouer.pack()
            frameRejouer.place(x=420, y=150)
        essai-=1



def regle():
    lesRegles()

motHasard=choix()

fenetrePrincipal=Tk()

fenetrePrincipal.title("Fandr's app")
fenetrePrincipal.geometry("720x400")
fenetrePrincipal.minsize(700,500)
fenetrePrincipal.maxsize(720,400)
fenetrePrincipal.iconbitmap("icon.ico")
fenetrePrincipal.config(background='#195c85')

#Titre
frameTitre = Frame(fenetrePrincipal,bg='#195c85',relief=SUNKEN,bd=0,highlightthickness=0)
titre = Label(frameTitre,text="Jeu du pendu",font=("Cooper Black",20,'italic'),bg='#195c85')
sousTitre = Label(frameTitre,text="Essayer de deviner le mot",font=("Arial",12,'italic'),bg='#195c85')
titre.pack()
sousTitre.pack()
frameTitre.place(x=450,y=0)

#image de fond
canvaImage = Canvas(fenetrePrincipal,width=400,height=500,bg='#195c85',bd=0,highlightthickness=0)
imageFond = PhotoImage(file="img.png").zoom(35).subsample(35)
canvaImage.create_image(200,250,image=imageFond)
canvaImage.place(x=0,y=0)

#Bloc affichage et input nom du joueur
frameAffichageNom = Frame(fenetrePrincipal,bg='#195c85',relief=SUNKEN,bd=0,highlightthickness=0)
labelNom = Label(frameAffichageNom,text="Veuillez entrer votre nom de joueur : ",font=("Arial",12,'italic'),bg='#195c85')
inputNom = Entry(frameAffichageNom)
boutonNom = Button(frameAffichageNom,text="Enregistrer nom",command=enregistrerNom,bg='#dbdcff',font=('Arial Black',8))
labelNom.pack()
inputNom.pack()
boutonNom.pack()
frameAffichageNom.place(x=420,y=150)

#Bloc affichage et input du jeu (le mot , les lettres)
frameAffichageJeu = Frame(fenetrePrincipal,bg='#195c85',relief=SUNKEN,bd=0,highlightthickness=0)
labelTexte1 = Label(frameAffichageJeu,text="",font=("Arial",12,'italic'),bg='#195c85')
inputLettre = Entry(frameAffichageJeu)
boutonValiderLettre = Button(frameAffichageJeu,text="Valider",command=validerLettre,bg='#dbdcff',font=('Arial Black',8))
labelAvertissement = Label(frameAffichageJeu,text="",font=("Arial",12,'italic'),fg='red',bg='#195c85')
boutonOk = Button(frameAffichageJeu,text="Ok",command=ok,bg='#dbdcff',font=('Arial Black',8))

#Rejouer
frameRejouer = Frame(fenetrePrincipal,bg='#195c85',relief=SUNKEN,bd=0,highlightthickness=0)
labelRejouer = Label(frameRejouer, text="Perdu, une prochaine fois peut-être. :)",fg='red', font=("Arial", 12, 'italic'), bg='#195c85')

#Bouton regle
bottonRegle = Button(fenetrePrincipal,text="Regles",command=regle,bg='#dbdcff',font=('Arial',10))
bottonRegle.place(x=650,y=450)

copyRight = Label(fenetrePrincipal,text="©CopyRight RAVELOHARISON Fandresena",bg='#195c85')
copyRight.place(x=0,y=480)

fenetrePrincipal.mainloop()