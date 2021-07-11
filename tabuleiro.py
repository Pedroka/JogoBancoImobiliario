import propriedade as p
import jogador as j
import random
from collections import OrderedDict

class Tabuleiro():
    
    # Inicializando o Tabuleiro #
    def __init__(self):
        self.bonus_volta = 100
        self.board = {}
        self.totalRodadas = 1000
        self.vencedor = []
        self.jogadoresDisponiveis = []
        self.partidasporTimeOut = 0

        # Criando as Propriedades #
        self.propriedades = [
            None,
            p.Propriedades(100, 50, 'Vila Mariana'),
            p.Propriedades(50, 45,  'Vila Joao'),
            p.Propriedades(150, 75, 'Morumbi'),
            p.Propriedades(75, 40,  'Jd. Macarenhas'),
            p.Propriedades(45, 60,  'Santa Maria'),
            p.Propriedades(35, 36,  'Pq. Santa Felícia'),
            p.Propriedades(60, 43,  'Pq. Faber'),
            p.Propriedades(80, 81,  'Iaquera'),
            p.Propriedades(66, 49,  'Pq Junqueira'),
            p.Propriedades(30, 38,  'Aparecida'),
            p.Propriedades(21, 35,  'São Martinho'),
            p.Propriedades(35, 36,  'São Roque'),
            p.Propriedades(100, 80, 'Jabaquara'),
            p.Propriedades(150, 75, 'Guarulhos'),
            p.Propriedades(90, 75,   'Pq. das Flores'),
            p.Propriedades(45, 48,  'Avenida da Saudade'),
            p.Propriedades(60, 45,  'Centro'),
            p.Propriedades(90, 84,  'Pq. Ibirapuera'),
            p.Propriedades(65, 42,  'Jd. Alvorada'),
            p.Propriedades(93, 36,  'Cidade Jardim')
        ]

        # Alocando as Propriedades em suas posições no Tabuleiro #
        for i in range(1,21):
            self.board.update({i:self.propriedades[i]})

        # Criando os jogadores #
        self.jogadores = [
            j.JogadorImpulsivo(),
            j.JogadorExigente(),
            j.JogadorCauteloso(),
            j.JogadorAleatorio()
        ]

    # Os metodos abaixo são exclusivos para a dinamica do game #
    def rolarDado(self):
        return random.randint(1, 6)


    def moverJogadorTabuleiro(self, jogador, dado):
        if ((jogador.posicao + dado)-20) < 0:
            jogador.atualizaPosicaoTabuleiro(jogador.posicao+dado)
        elif ((jogador.posicao + dado)-20) == 0:
            jogador.atualizaPosicaoTabuleiro(20)
        else:
            jogador.atualizaSaldo(self.bonus_volta)
            jogador.atualizaPosicaoTabuleiro(((jogador.posicao+dado)-20))


    def comprarPropriedade(self, jogador, propriedade):
        if jogador.estrategiaCompra(propriedade):
            if jogador.validaSaldo():
                if jogador.saldoDinheiro >= propriedade.custo_venda:
                    jogador.atualizaSaldo(-propriedade.custo_venda)
                    propriedade.atualizaPropriedade(jogador)
            else:
                self.removePropriedades(jogador)
            

    def pagarAluguel(self, jogador, propriedade):
        if jogador != propriedade.jogador:
            if jogador.validaSaldo():
                if jogador.saldoDinheiro >= propriedade.vlr_aluguel:
                    jogador.atualizaSaldo(-propriedade.vlr_aluguel)
                    propriedade.jogador.atualizaSaldo(propriedade.vlr_aluguel)
                else:
                    self.removePropriedades(jogador)    
            else:
                self.removePropriedades(jogador)


    def removePropriedades(self, jogador):
        for prop in self.propriedades:
            if prop != None:
                if jogador == prop.jogador:
                    prop.atualizaPropriedade(None)


    def checaRodada(self, rodada):
        if rodada <= self.totalRodadas:
            self.jogadoresDisponiveis = []
            for j in self.jogadores:
                if j.validaSaldo():
                    self.jogadoresDisponiveis.append(j)
                else:
                    self.removePropriedades(j)

            if len(self.jogadoresDisponiveis) == 1:
                self.jogadoresDisponiveis[0].qtdVitorias += 1
                return False, self.jogadoresDisponiveis[0]
            else:
                return True, self.jogadoresDisponiveis
        else:
            self.partidasporTimeOut += 1
            for j in self.jogadoresDisponiveis:
                self.vencedor.append({"jogador":j,"saldo":j.saldoDinheiro})
                self.vencedor = sorted(self.vencedor, key=lambda k: k['saldo'])
                self.vencedor[len(self.vencedor)-1]['jogador'].qtdVitorias += 1

                return False, self.vencedor[len(self.vencedor)-1]['jogador']
            
            