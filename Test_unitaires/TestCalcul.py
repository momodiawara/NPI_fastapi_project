import unittest
import sys
import os

# Ajoutez le répertoire Controler au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../controler')))

from controler import Calcul  # Importation de la classe


class TestCalcul(unittest.TestCase):

    def setUp(self):
        self.calcul = Calcul()

    def testAddition(self):
        result = self.calcul.evaluation("2 3 +")
        self.assertEqual(result, 5)

    def testSoustraction(self):
        result = self.calcul.evaluation("5 2 -")
        self.assertEqual(result, 3)

    def testMultiplication(self):
        result = self.calcul.evaluation("4 5 *")
        self.assertEqual(result, 20)

    def testDivision(self):
        result = self.calcul.evaluation("9 3 /")
        self.assertEqual(result, 3)

    def testDivisionParZero(self):
        result = self.calcul.evaluation("4 0 /")
        self.assertEqual(result, "Erreur : Division par zéro")

    def testPuissance(self):
        result = self.calcul.evaluation("2 3 ^")
        self.assertEqual(result, 8.0)

    def testModulo(self):
        result = self.calcul.evaluation("4 3 %")
        self.assertEqual(result, 1)

    def testExpressionMalFormee(self):
        result = self.calcul.evaluation("2 +")
        self.assertEqual(result, "Erreur : Expression mal formée, pas assez d'opérandes pour l'opérateur.")

    def testTropOperandes(self):
        result = self.calcul.evaluation("2 3 + 4")
        self.assertEqual(result, "Erreur : Expression mal formée, trop d'opérandes ou opérateurs manquants.")

    def testInfixSimpleAddition(self):
        expression = "3 4 +"
        infix_expression = self.calcul.normalisation(expression)
        self.assertEqual(infix_expression, "(3 + 4)")

    def testInfixComplexExpression(self):
        expression = "3 4 + 2 * 7 /"
        infix_expression = self.calcul.normalisation(expression)
        self.assertEqual(infix_expression, "(((3 + 4) * 2) / 7)")

    def testInfixSubtraction(self):
        expression = "5 3 -"
        infix_expression = self.calcul.normalisation(expression)
        self.assertEqual(infix_expression, "(5 - 3)")



if __name__ == "__main__":
    unittest.main()
