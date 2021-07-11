
import jogador as j
class Propriedades():

    def __init__(self, custo_venda, vlr_aluguel, nome_imovel, jogador=None):
        self.custo_venda = custo_venda
        self.vlr_aluguel = vlr_aluguel
        self.jogador = jogador
        self.nome_imovel = nome_imovel
    
    def checaDisponibilidade(self):
        return False if self.jogador != None else True
    
    def atualizaPropriedade(self, jogador):
        self.jogador = jogador