#!/usr/bin/python

import sys

from KmpAlgorithm import KmpAlgorithm

#Retourne vraie si l'expression reguliere est reduite à une suite de concatenations
def estSuiteConcatenations(regEx : str):
    for i in range(len(regEx)):
        if (((regEx[i] == '*') | (regEx[i] == '|')) | (regEx[i] == '.')):
            return False
    return True

# Ouvre le fichier avec le nom "fileName" passé en parametre, recupere
# le texte dans le fichier et le retourne
def fileToText(fileName : str):
    f = open(fileName, "r")
    return f.read()

# Methode qui imprime la matrice representant un automate

# Methode qui imprime sur la sortie standard les lignes résutants de la
# recherche mené avec l'une des deux methodes.
def printLignes(lignes):
    for ligne in lignes:
        print(ligne)


def main():
    if (len(sys.argv) < 3):
        print("Erreur : veuillez introduire l'expression reguliere et le fichier txt")
    elif((len(sys.argv[1]) == 0) | (len(sys.argv[2]) == 0)):
        print("Erreur : veuillez introduire l'expression reguliere et le fichier txt")
    else:
        print("____________________________________")
        print("regEx : "+ sys.argv[1])
        print("____________________________________")
        if (estSuiteConcatenations(sys.argv[1])):
            print("=========Recherche avec KMP=========")
            regEx : str = sys.argv[1]
            text : str = fileToText(sys.argv[2])
            kmp = KmpAlgorithm(regEx, text)
            kmp.generateFunctor()
            # to continue
        else:
            print("=========Recherche avec automate=========")
            regEx : str = sys.argv[1]
            # to conitnue

main()