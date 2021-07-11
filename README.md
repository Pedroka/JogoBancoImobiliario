## Utilizacao:

Executando Testes:
```bash
python3 -m unnittest
```

Executando Jogo:
```bash
python3 main.py
```

## Explicando a Implementação:

1. Jogador.py:
- O arquivo jogador.py fica responsável por toda a criação dos Jogadores (Impulsivo, Exigente, Cauteloso e Aleatório) e definição da Estratégia de Compra de cada um. Além possui métodos de validação/atualização de Saldo e atualização da posição no Tabuleiro.

2. Propriedade.py
- O arquivo propriedade.py possui classes e métodos que são responsáveis pela criação das Propriedades dentro do Tabuleiro. Além disso possui outros métodos para checagem da disponibilidade de compra, e atualização do proprietário.

3. Tabuleiro.py
- O arquivo tabuleiro.py possui classes e métodos referentes à dinamica do Jogo. É a partir dele que montamos o nosso tabuleiro e criamos nossas propriedades e jogadores que serão parte do game. É nesse arquivo que foi implementada toda a dinamica de rolagem de dado, movimentação, compra e aluguel de propriedades.

4. Game.py
- O arquivo game.py é responsável por toda a montagem das rodadas e execução das partidas.

5. Main.py
- Execução da simulação das 300 partidas e exibição dos resultados.