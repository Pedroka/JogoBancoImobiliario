import tabuleiro as tb
import propriedade as p
import jogador as j

class BancoImobiliario():

    def __init__(self):
        self.tab = tb.Tabuleiro()
    
    def executeGame(self):
        rodada = 1
        while (rodada <= 1000):
            rodada += 1
            game_on, jogadores = self.tab.checaRodada(rodada)
            if game_on:
                for j in jogadores:
                    j.turnosJogados += 1
                    dado = self.tab.rolarDado()
                    self.tab.moverJogadorTabuleiro(j,dado)

                    if j.posicao in self.tab.board.keys():
                        if self.tab.propriedades[j.posicao].checaDisponibilidade():
                            self.tab.comprarPropriedade(j, self.tab.propriedades[j.posicao])
                        else:
                            self.tab.pagarAluguel(j, self.tab.propriedades[j.posicao])
            else:
                return jogadores

        game_on, jogadores = self.tab.checaRodada(rodada)
        return jogadores
        
            