class KmpAlgorithm:

    def __init__(self, regEx: str, text: str):

        # Expression reguliere
        self.regEx = regEx
        # Le text dans lequel effectuer la recherche
        self.text = text
        # Une liste ordonée des caractères de l'expression reguliere
        self.Factor = []
        # Une liste indiquant pour chaque position un décalage
        self.CarryOver = []

    # Convertie l'expression reguliere en une liste ordonée des caractères
    # (crée le Factor)
    def generateFunctor(self):
        for i in range(len(self.regEx)):
            self.Factor.insert(i, self.regEx[i])
        print(self.Factor)