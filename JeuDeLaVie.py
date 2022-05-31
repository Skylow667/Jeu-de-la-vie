
import os
from re import T
import time
import copy
from tkinter import * 



class JeuDeLaVie:
    def __init__(self, tableau):
        """
        Affecte un tableau à deux dimensions à l'attribut tableau
    
        :param tableau: tableau à deux dimensions
        """
        
        self.tableau=tableau
        self.nb_lignes=len(tableau)
        self.nb_colonnes=len(tableau[0])
        self.Vivant=input("Choisi ton symbole pour les celle vivantes (ex: *): ")
        self.Mort=input("Choisi ton symbole pour les cellules mortes (ex: .): ")

    def affiche(self):
        """
        Affiche le tableau
        """
        os.system('cls')
        for i in range(self.nb_lignes):
            for j in range(self.nb_colonnes):
                if self.tableau[i][j]==1:
                    print(self.Vivant, end="")
                else:
                    print(self.Mort, end="")
            print()
        print()



    def valeur_case(self, i, j):
        """
        Renvoie la valeur de la case [i][j] ou 0 si la case n'existe pas
        """
        if i>=0 and i<self.nb_lignes and j>=0 and j<self.nb_colonnes:
            return self.tableau[i][j]
        else:
            return 0

    def total_voisins(self, i, j):
        """
        Renvoie la somme des valeurs des voisins de la case [i][j]
        """
        total=0
        for k in range(-1,2):
            for l in range(-1,2):
                total+=self.valeur_case(i+k,j+l)
        total-=self.valeur_case(i,j)
        return total


    def run(self, nombre_tours, delai):
        """
        Méthode principale du jeu
    
        Fait tourner le jeu de la vie pendant nombre_tours
        Elle rafraîchit l'affichage à chaque tour et
        attend delai entre chaque tour
    
        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d'attente en secondes entre chaque tour
        """
        
        for i in range(nombre_tours):
            self.tour()
            time.sleep(delai)

    def resultat(self, valeur_case, total_voisins):
        """
        Renvoie la valeur suivante d'une cellule
    
        :param valeur_case: la valeur de la cellule (0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant
        """
        
        if valeur_case==1:
            if total_voisins==2 or total_voisins==3:
                return 1
            else:
                return 0
        else:
            if total_voisins==3:
                return 1
            else:
                return 0



        

    def tour(self):
        """
        Met à jour toutes les cellules du tableau en respectant
        les règles du jeu de la vie
        """
        tableau_suivant=copy.deepcopy(self.tableau)
        for i in range(self.nb_lignes):
            for j in range(self.nb_colonnes):
                total_voisins=self.total_voisins(i,j)
                tableau_suivant[i][j]=self.resultat(self.tableau[i][j], total_voisins)
        if self.tableau==tableau_suivant:
            print("Il n'y a pas de changement")
            exit()
        self.tableau=tableau_suivant
        self.affiche()




tableau = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]



mon_jeu = JeuDeLaVie(tableau)
mon_jeu.run(200, 0.1)



    
