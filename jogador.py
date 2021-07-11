from abc import ABC, abstractmethod
import random

class Jogador(ABC):

    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
        self.saldoDinheiro = 300
        self.posicao = 0
        self.turnosJogados = 0
        self.qtdVitorias = 0

    @abstractmethod
    def estrategiaCompra(self):
        pass

    def validaSaldo(self):
        if self.saldoDinheiro > 0:
            return True
        else:
            return False

    def atualizaSaldo(self, vlr):
        self.saldoDinheiro += vlr
    
    def atualizaPosicaoTabuleiro(self, posicao):
        self.posicao = posicao

class JogadorImpulsivo(Jogador):

    def __init__(self, tipo='Impulsivo', cor='Vermelha'):
        super().__init__(tipo, cor)
        self.tipo = tipo
        self.cor = cor

    def estrategiaCompra(self, propriedade):
        return True

class JogadorExigente(Jogador):

    def __init__(self, tipo='Exigente', cor='Azul'):
        super().__init__(tipo, cor)
        self.tipo = tipo
        self.cor = cor

    def estrategiaCompra(self, propriedade):
        return True if propriedade.vlr_aluguel > 50 else False

class JogadorCauteloso(Jogador):

    def __init__(self, tipo='Cauteloso', cor='Amarelo'):
        super().__init__(tipo, cor)
        self.tipo = tipo
        self.cor = cor

    def estrategiaCompra(self, propriedade):
        return True if self.saldoDinheiro-propriedade.custo_venda >= 80 else False

class JogadorAleatorio(Jogador):
    import random

    def __init__(self, tipo='Aleatorio', cor='Verde'):
        super().__init__(tipo, cor)
        self.tipo = tipo
        self.cor = cor

    def estrategiaCompra(self, propriedade):
        return True if random.randint(0, 2) > 1 else False