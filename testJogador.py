import unittest
from unittest.mock import MagicMock
import jogador as j
import propriedade as p

class JogadorImpulsivo(unittest.TestCase):
    
    def setUp(self):
        self.Impulsivo = j.JogadorImpulsivo()
        self.Propriedade = p.Propriedades(50, 100, 'Teste')

    
    def testDeveComprar(self):
        if self.Impulsivo.validaSaldo():
            deveComprar = self.Impulsivo.estrategiaCompra(self.Propriedade)
        else:
            deveComprar = False

        self.assertTrue(deveComprar)

    def testNaoDeveComprar(self):
        self.Impulsivo.saldoDinheiro = 0
        if self.Impulsivo.validaSaldo():
            deveComprar = self.Impulsivo.estrategiaCompra(self.Propriedade)
        else:
            deveComprar = False

        self.assertFalse(deveComprar)

class JogadorExigente(unittest.TestCase):
    
    def setUp(self):
        self.Exigente = j.JogadorExigente()

    
    def testDeveComprar(self):
        Propriedade = p.Propriedades(50, 100, 'Teste')
        if self.Exigente.validaSaldo():
            deveComprar = self.Exigente.estrategiaCompra(Propriedade)
        else:
            deveComprar = False

        self.assertTrue(deveComprar)

    def testNaoDeveComprar(self):
        Propriedade = p.Propriedades(100, 40, 'Teste')
        if self.Exigente.validaSaldo():
            deveComprar = self.Exigente.estrategiaCompra(Propriedade)
        else:
            deveComprar = False

        self.assertFalse(deveComprar)


class JogadorCauteloso(unittest.TestCase):
    
    def setUp(self):
        self.Cauteloso = j.JogadorCauteloso()

    
    def testDeveComprar(self):
        Propriedade = p.Propriedades(50, 100, 'Teste')
        if self.Cauteloso.validaSaldo():
            deveComprar = self.Cauteloso.estrategiaCompra(Propriedade)
        else:
            deveComprar = False

        self.assertTrue(deveComprar)

    def testNaoDeveComprar(self):
        Propriedade = p.Propriedades(250, 40, 'Teste')
        if self.Cauteloso.validaSaldo():
            deveComprar = self.Cauteloso.estrategiaCompra(Propriedade)
        else:
            deveComprar = False

        self.assertFalse(deveComprar)


class JogadorAleatorio(unittest.TestCase):
    
    def setUp(self):
        self.Aleatorio = j.JogadorAleatorio()
        self.Propriedade = p.Propriedades(50, 100, 'Teste')

    def testNaoDeveComprar(self):
        self.Aleatorio.saldoDinheiro = 0
        if self.Aleatorio.validaSaldo():
            deveComprar = self.Aleatorio.estrategiaCompra(self.Propriedade)
        else:
            deveComprar = False

        self.assertFalse(deveComprar)

        