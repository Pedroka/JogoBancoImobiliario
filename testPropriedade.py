import unittest
import propriedade as p
import jogador as j

class PropriedadeTest(unittest.TestCase):
    def setUp(self):
        self.propriedade = p.Propriedades(100,50,'Teste')
    
    def testCriaPropriedade(self):
        propEsperada = {
            "custo_venda": 100,
            "vlr_aluguel": 50,
            "nome_imovel": "Teste",
            "jogador": None
        }

        self.assertEqual(propEsperada, self.propriedade.__dict__)
    
    def testAtualizaProprietario(self):
        self.propriedade.atualizaPropriedade(j.JogadorImpulsivo())
    
    def testPropriedadeNaoDisponivel(self):
        self.propriedade.atualizaPropriedade(j.JogadorImpulsivo())
        disponivel = self.propriedade.checaDisponibilidade()

        self.assertFalse(disponivel)

    def testPropriedadeDisponivel(self):
        disponivel = self.propriedade.checaDisponibilidade()

        self.assertTrue(disponivel)