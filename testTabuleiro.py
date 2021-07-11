import unittest
import tabuleiro as t
import jogador as j
import propriedade as p

class TabuleiroTest(unittest.TestCase):

    def setUp(self):
        self.jogador = j.JogadorImpulsivo()
        self.propriedade = p.Propriedades(100, 50, 'Teste')
        self.tabuleiro = t.Tabuleiro()
    
    def testRolarDado(self):
        validaDado = True if self.tabuleiro.rolarDado() in [1,2,3,4,5,6] else False

        self.assertTrue(validaDado)
    
    def testMoverJogadorSucesso(self):
        self.tabuleiro.moverJogadorTabuleiro(self.jogador, 5)
        validaPosicao = True if self.jogador.posicao > 0 else False

        self.assertTrue(validaPosicao)
    
    def testMoverJogadorFalha(self):
        self.tabuleiro.moverJogadorTabuleiro(self.jogador, 0)
        validaPosicao = True if self.jogador.posicao > 0 else False

        self.assertFalse(validaPosicao)
    
    def testComprarPropriedade(self):
        self.tabuleiro.comprarPropriedade(self.jogador, self.propriedade)
        validaCompra = True if self.jogador == self.propriedade.jogador else False

        self.assertTrue(validaCompra)

    def testCobrarAluguelPropriedade(self):
        self.propriedade.jogador = j.JogadorCauteloso()
        self.tabuleiro.pagarAluguel(self.jogador, self.propriedade)

        validaAluguel = True if self.jogador.saldoDinheiro < 300 else False

        self.assertTrue(validaAluguel)