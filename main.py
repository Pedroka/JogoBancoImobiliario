import game as g

simulacao = 1
PartidasporTimeOut = 0
qtdTurnos = 0
vencedores = []

while (simulacao <= 300):
    gg = g.BancoImobiliario()
    vencedores.append(gg.executeGame().tipo)
    PartidasporTimeOut += gg.tab.partidasporTimeOut
    for j in gg.tab.jogadores:
        qtdTurnos += j.turnosJogados
    simulacao += 1
print('Executando Simulação com 300 Partidas:')
print(f' Partidas por TimeOut: {PartidasporTimeOut}')
print(f' Média de Turnos: {(qtdTurnos/1000)}')
print(' Percentual de Vitórias por Comportamento e Comportamento mais Vencedor:')
print(f"  Impulsivo: {(vencedores.count('Impulsivo')*100)/300}%")
print(f"  Exigente: {(vencedores.count('Exigente')*100)/300}%")
print(f"  Cauteloso: {(vencedores.count('Cauteloso')*100)/300}%")
print(f"  Aleatorio: {(vencedores.count('Aleatorio')*100)/300}%")
    
