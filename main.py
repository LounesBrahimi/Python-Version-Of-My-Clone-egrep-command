

#Retourne vraie si l'expression reguliere est reduite à une suite de concatenations
def estSuiteConcatenations(regEx : str):
    for i in range(len(regEx)):
        if (((regEx[i] == '*') | (regEx[i] == '|')) | (regEx[i] == '.')):
            return False
    return True


#print(estSuiteConcatenations("eB(oo)*k"))
#print(estSuiteConcatenations("eBook"))
