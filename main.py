

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



#print(estSuiteConcatenations("eB(oo)*k"))
#print(estSuiteConcatenations("eBook"))
print(fileToText("ebook1.txt"))

