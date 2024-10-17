import math

class Calcul:
    
    # Le constructeur avec un attribut privés
    def __init__(self):
        self.__pile = []

    # Les opérations de base
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erreur : Division par zéro"

    def puissance(self, a, b):
        return math.pow(a, b)

    def modulo(self, a, b):
        return a % b

    def default_operation(self, a, b):
        return "Opération non reconnue"

    # Le dictionnaire agissant comme un switch
    def _switch_operation(self, operator, a, b):
        switcher = {
            '+': self.addition,
            '-': self.soustraction,
            '*': self.multiplication,
            '/': self.division,
            '^': self.puissance,
            '%': self.modulo
        }
        # Récupère la fonction correspondant à l'opérateur et passe les deux arguments
        return switcher.get(operator, self.default_operation)(a, b)

    def evaluation(self, expression):

        #Évaluer une expression en notation polonaise inverse avec gestion d'erreurs.

        try:

            # divise tous les mots en une chaîne séparée par des espaces
            expression = expression.split()
            
            for element in expression:

                # vérifier si l'élément est un entier
                if element.isdigit():  
                    self.__pile.append(int(element))

                # Sinon, c'est un opérateur( + ou - ou * ou / ou ^ ou % )
                else:
                    # S'il y a moins de 2 éléments dans la pile, il manque des opérandes
                    if len(self.__pile) < 2:
                        raise ValueError("Expression mal formée, pas assez d'opérandes pour l'opérateur.")
                    
                    valeur_a = self.__pile.pop()
                    valeur_b = self.__pile.pop()
 
                    result = self._switch_operation(element, valeur_b, valeur_a)
                    self.__pile.append(result)

            if len(self.__pile) != 1:
                raise ValueError("Expression mal formée, trop d'opérandes ou opérateurs manquants.")
            
            return self.__pile.pop()

        except ZeroDivisionError:
            return "Erreur : Division par zéro."
        except ValueError as e:
            return f"Erreur : {e}"


    def normalisation(self, expression):

        maList = []        

        try :
            for elt in expression.split():

                if elt.isdigit():  
                    maList.append(elt)

                else:                    

                    try :
                        valeur_b = maList.pop()
                        valeur_a = maList.pop()
                    except IndexError:
                        return ""

                    newEpression = f"({valeur_a} {elt} {valeur_b})"
                    maList += [newEpression]

            return maList[0] if maList else ""

        except Exception as e:
            return f"Erreur : {e}"
    
        
