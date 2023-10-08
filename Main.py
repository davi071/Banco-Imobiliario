# Importação
from copy import deepcopy
from random import shuffle, randint
from Script.Propriedade import aluguel, lugar
from Script.Sorte_ou_Revez import sorte_ou_revez
# Configuração do jogo 
traço = '-=' * 30
traço1 = '-' * 60
i = 0 # Indicador de quem é a vez de jogar
rodada = 1
total_rodada = 1000 # Limite total de rodada
automático = 1 # 0 é manual, 1 automático
quant_preso = (3) + 1 # Quantidade de rodada preso
# Criação do personagem
personagem = [] # 0-posição, 1-nome, 2-dinheiro, 3-propriedade, 4-prisão, 5-automático, 6-hábias_corpus, 7-propriedade_empresa
bkp_personagem = [] # Faz backup dos personagem
personagem.append([0,'David',2500,[[0,0]],0,automático,0,[]])
personagem.append([0,'Maria',2500,[[0,0]],0,automático,0,[]])
# Estatística
estatística_real =  []
compra_lote = []
compra_casa = []
aluguel_jogador = []
# DEFS
def dados():
    d0 = randint(1,6)
    d1 = randint(1,6)
    d2 = d0 + d1
    return d0,d1,d2
# Logica do jogo
while True:
    print(traço)
    menu_jogo = str(input('''[ 0 ] Sair
[ 1 ] Jogar
[ 2 ] Configuração
[ 3 ] Estatística
Digite aqui: '''))
    if menu_jogo.isnumeric() == True:
        menu_jogo = int(menu_jogo)
        if menu_jogo == 0:
            print('Fim de jogo')
            break
# Inicio do jogo
        elif menu_jogo == 1:
            bkp_personagem = deepcopy(personagem) # Copia toda a ficha dos jogadores
            shuffle(personagem) # Aleatoriza jogadores
            for a in range(0,len(personagem)):
                print(f'{1+a}º {personagem[a][1]}')
            while True:
                print(traço)
                if len(personagem) > 1: # Verifica se tem mais de dois jogadores
                    if i >= len(personagem):
                        i -= int(len(personagem))
                    print(f'Esta na vez de {personagem[i][1]}, você esta em {lugar(personagem[i][0])[1]}, casa:{personagem[i][0]}')
                    print(f'Dinheiro: R${personagem[i][2]} round: {rodada}º')
                    print(f'Propriedades: ',end='')
                    if personagem[i][3][0][0] != 0:
                        for a in range(0,len(personagem[i][3])):
                            print(f'\'{lugar(personagem[i][3][a][0])[1]}, casas:{personagem[i][3][a][1]}\'',end='')
                        print('')
                    else:
                        print('Nenhum')
                    if personagem[i][5] == 0: # jogada manual
                        jogo = str(input('[ Enter ] Jogar os dados: '))
                    else: # jogada automática
                        print('Jogando os dados:')
                        jogo = '' # Jogada automática
                    if jogo.isnumeric() == True:
                        jogo = int(jogo)
                        if jogo == 0:
                            break
                    dado = dados() # Principal rolagem dos dados
                    if personagem[i][4] == 0: # Primeira verificação, não prisão
                        print(traço1)
                        personagem[i][0] += dado[2]
                        if personagem[i][0] >= 40:
                            personagem[i][0] -= 40
                            personagem[i][2] += 200
                            print('Passou pelo inicio ganha, R$200')
                        print(f'Dados: {dado[0]} + {dado[1]} = {dado[2]}')
                        print(f'Avançou até \"{lugar(personagem[i][0])[1]}\"')
# Verificação da cadeia
                    elif personagem[i][4] > 0: # Preso
                        print(traço1)
                        if personagem[i][5] == 0: # Manual
                            if dado[0] == dado[1]: # Primeira verificação do dado
                                personagem[i][0] = 10
                                personagem[i][4] = 0
                                print(f'{dado[0]} e {dado[1]}, são iguais e saiu da cadeia')
                            elif dado[0] != dado[1]:
                                while True:
                                    print(f'{dado[0]} e {dado[1]}, não são iguais')
                                    #com hábias e com dinheiro
                                    if personagem[i][2] >= 50 and personagem[i][6] > 0:
                                        negociação2 = str(input(f'''Falta {personagem[i][4]}, rodadas para sair
[ Enter ] Continuar
[ 1 ] Usar hábias corpus
[ 2 ] Pagar R$50
Digite aqui: '''))
                                        if negociação2 == '':
                                            print(f'{personagem[i][1]}, apenas continuou')
                                            break
                                        elif negociação2 == '1':
                                            personagem[i][0] = 10
                                            personagem[i][6] - 1
                                            print(f'{personagem[i][1]}, usou hábias corpus e saiu da cadeia')
                                            break
                                        elif negociação2 == '2':
                                            personagem[i][0] = 10
                                            personagem[i][2] - 50
                                            print(f'{personagem[i][1]},pagou R$50 e saiu da cadeia')
                                            break
                                    #sem hábias e com dinheiro
                                    if personagem[i][2] >= 50 and personagem[i][6] == 0:
                                        negociação2 = str(input(f'''Falta {personagem[i][4]}, rodadas para sair
[ Enter ] Continuar
[ 1 ] Pagar R$50
Digite aqui: '''))
                                        if negociação2 == '':
                                            print(f'{personagem[i][1]}, apenas continuou')
                                            break
                                        elif negociação2 == '1':
                                            personagem[i][0] = 10
                                            personagem[i][2] - 50
                                            print(f'{personagem[i][1]},pagou R$50 e saiu da cadeia')
                                            break
                                    #com hábias e sem dinheiro
                                    if personagem[i][2] < 50 and personagem[i][6] > 0:
                                        negociação = str(input(f'''Falta {personagem[i][4]}, rodadas para sair
[ Enter ] Continuar
[ 1 ] Usar hábias corpus
Digite aqui: '''))
                                        if negociação2 == '':
                                            print(f'{personagem[i][1]}, apenas continuou')
                                            break
                                        elif negociação2 == '1':
                                            personagem[i][0] = 10
                                            personagem[i][6] - 1
                                            print(f'{personagem[i][1]}, usou hábias corpus e saiu da cadeia')
                                            break
                                    #sem hábias e sem dinheiro
                                    if personagem[i][2] < 50 and personagem[i][6] == 0:
                                        print(f'Falta {personagem[i][4]}, rodadas para sair')
                                        print(f'{personagem[i][1]}, não tem dinheiro, não possui hábias corpus, apenas continuou')
                                        break
                        elif personagem[i][5] == 1: # Automático
                            print(f'Falta {personagem[i][4]}, rodadas para sair')
                            if dado[0] == dado[1]: # Primeira verificação do dado
                                personagem[i][0] = 10
                                personagem[i][4] = 0
                                print(f'{dado[0]} e {dado[1]}, são iguais e saiu da cadeia')
                            elif personagem[i][6] > 0: # Usar hábias corpus
                                personagem[i][6] - 1
                                print(f'{personagem[i][1]}, usou hábias corpus e saiu da cadeia')
                            elif rodada <= 50 and personagem[i][2] >= 50: # Abaixo do round 50 e se tiver dinheiro sai
                                personagem[i][0] = 10
                                personagem[i][2] - 50
                                print(f'{personagem[i][1]},pagou R$50 e saiu da cadeia')
                            else:
                                print(f'{personagem[i][1]}, apenas continua')
# Verificação
                    if lugar(personagem[i][0])[0] == 0:
                        print('Ferias/Sem ação')
# Verificação das propriedades
                    elif lugar(personagem[i][0])[0] == 1:
                        p = 0 # ninguém possui a propriedade
                        for a in range(0,len(personagem)): # Para cada jogador
                            for b in range(0,len(personagem[a][3])): # Para cada propriedade
                                if personagem[i][0] == personagem[a][3][b][0]:
                                    if personagem[a] == personagem[i]: # Caso você seja o dono
                                        p = 2
                                    else: # Caso você não seja o dono
                                        p = 1
                        if p == 0: # Propriedade sem dono
                            if personagem[i][2] >= lugar(personagem[i][0])[2]: # Verificação de dinheiro
                                while True:
                                    print(f'Dinheiro: R${personagem[i][2]}')
                                    print(traço1)
                                    if personagem[i][5] == 0: # Manual
                                        negociação = str(input(f'''Valor da propriedade R${lugar(personagem[i][0])[2]}
[ S ] Comprar
[ N ] Não comprar
Digite aqui: ''')).upper()
                                    elif personagem[i][5] == 1: # Automático
                                        print(f'Valor da propriedade R${lugar(personagem[i][0])[2]}')
                                        negociação = 'S'
                                    if negociação == 'S':
                                        propriedade = list(personagem[i][3])
                                        if propriedade[0] == [0,0]:
                                            del(propriedade[0])
                                        propriedade.append([personagem[i][0],0])
                                        personagem[i][3] = propriedade
                                        personagem[i][2] -= lugar(personagem[i][0])[2] # Desconta valor da propriedade adquirida
                                        print(f'{personagem[i][1]}, comprou: {lugar(personagem[i][0])[1]}, dinheiro atual: R${personagem[i][2]}')
                                        compra_lote.append(f'R:{rodada}, {personagem[i][1]}, comprou: {lugar(personagem[i][0])[1]}, valor: R${-lugar(personagem[i][0])[2]}')
                                        estatística_real += [personagem[i][1],-lugar(personagem[i][0])[2]]
                                        break
                                    elif negociação == 'N':
                                        break
                            else:
                                print('Você não possui dinheiro suficiente para comprar essa propriedade')
                        elif p == 1: # Propriedade com dono
                            print('Propriedade tem dono')
                            
                            for a in range(0,len(personagem)): # Cada jogador
                                for b in range(0, len(personagem[a][3])): # Cada propriedade
                                    if personagem[i][0] == personagem[a][3][b][0]: # Jogador atual esta na propriedade do dono do terreno
                                        personagem[i][2] -= aluguel(personagem[i][0])[personagem[a][3][b][1]]
                                        personagem[a][2] += aluguel(personagem[i][0])[personagem[a][3][b][1]]
                                        print(f'{personagem[i][1]}, pagou aluguel para {personagem[a][1]}, de R${aluguel(personagem[i][0])[personagem[a][3][b][1]]}')                    
                                        aluguel_jogador.append(f'R:{rodada}, {personagem[i][1]}, pagou > {personagem[a][1]}, de R${aluguel(personagem[i][0])[personagem[a][3][b][1]]}')
                        elif p == 2: # Compra das casas em sua propriedade
                            print('Você é o dono da propriedade')
                            if personagem[i][2] >= 200:
                                for a in range(0,len(personagem[i][3])):
                                    if personagem[i][0] == personagem[i][3][a][0]:
                                        if personagem[i][3][a][1] <= 4: # Condição se ainda não tem as 5 casas
                                            while True:
                                                print(traço1)
                                                if personagem[i][5] == 0: # Manual
                                                    negociação1 = '' # Caso vá sem uma string
                                                    negociação1 = str(input(f'''Dinheiro R${personagem[i][2]}, cada casa vale R$ 200
[ S ] Comprar
[ N ] Não comprar
Digite aqui: ''')).upper()
                                                elif personagem[i][5] == 1: # Automático
                                                    negociação1 = 'S'
                                                if negociação1 == 'S':
                                                    for a in range(0,len(personagem[i][3])):
                                                        if personagem[i][0] == personagem[i][3][a][0]:
                                                            personagem[i][3][a][1] += 1 # Adiciona uma casa
                                                            print(f'{personagem[i][1]}, comprou uma casa em {lugar(personagem[i][3][a][0])[1]}, valor R$200')
                                                            compra_casa.append(f'R:{rodada}, {personagem[i][1]}, comprou casa em: {lugar(personagem[i][0])[1]}, valor: R$200')
                                                            break
                                                    break
                                                elif negociação1 == 'N':
                                                    break
# Verificação da/s empresa/s
                    elif lugar(personagem[i][0])[0] == 2:
                    # Empresa
                        pe = 0
                        for a in range(0,len(personagem)): # Para cada jogador
                            for b in range(0,len(personagem[a][7])): # Para cada propriedade da empresa
                                if personagem[i][0] == personagem[a][7][b][0]:
                                    if personagem[a] == personagem[i]: # Caso você seja o dono
                                        pe = 2
                                    else: # Caso você não seja o dono
                                        pe = 1
                        if pe == 0: # Sem dono
                            if personagem[i][2] >= lugar(personagem[i][0])[2]: # Verificação de dinheiro
                                while True:
                                    print(f'Dinheiro: R${personagem[i][2]}')
                                    print(traço1)
                                    if personagem[i][5] == 0: # Manual
                                        negociação = str(input(f'''Valor da empresa R${lugar(personagem[i][0])[2]}
[ S ] Comprar
[ N ] Não comprar
Digite aqui: ''')).upper()
                                    elif personagem[i][5] == 1: # Automático
                                        print(f'Valor da propriedade R${lugar(personagem[i][0])[2]}')
                                        negociação = 'S'
                                    if negociação == 'S':
                                        propriedade = list(personagem[i][7])
                                        #if propriedade[] == []:
                                        #    del(propriedade[0])
                                        propriedade.append([personagem[i][0]])
                                        personagem[i][7] = propriedade
                                        personagem[i][2] -= lugar(personagem[i][0])[2] # Desconta valor da empresa adquirida
                                        print(f'{personagem[i][1]}, comprou: {lugar(personagem[i][0])[1]}, dinheiro atual: R${personagem[i][2]}')
                                        compra_lote.append(f'R:{rodada}, {personagem[i][1]}, comprou: {lugar(personagem[i][0])[1]}, valor: R${-lugar(personagem[i][0])[2]}')
                                        estatística_real += [personagem[i][1],-lugar(personagem[i][0])[2]]
                                        break
                                    elif negociação == 'N':
                                        break
                            else:
                                print('Você não possui dinheiro suficiente para comprar essa empresa')
                        elif pe == 1: # Tem dono
                            print('Tem dono')
                            for a in range(0,len(personagem)): # Cada jogador
                                for b in range(0, len(personagem[a][7])): # Cada propriedade
                                    if personagem[i][0] == personagem[a][7][b][0]: # Jogador atual esta na empresa do dono do terreno
                                        #personagem[i][2] -= aluguel(personagem[i][0])[personagem[a][3][b][1]]
                                        #personagem[a][2] += aluguel(personagem[i][0])[personagem[a][3][b][1]]
                                        #print(f'{personagem[i][1]}, pagou aluguel para {personagem[a][1]}, de R${aluguel(personagem[i][0])[personagem[a][3][b][1]]}')                    
                                        #aluguel_jogador.append(f'R:{rodada}, {personagem[i][1]}, pagou > {personagem[a][1]}, de R${aluguel(personagem[i][0])[personagem[a][3][b][1]]}')
                                        #soma = dado[2] # Soma dos dados
                                        soma_empresa = dado[2] * aluguel(personagem[i][0])[0] # soma dos dados * x
                                        personagem[i][2] -= soma_empresa
                                        personagem[a][2] += soma_empresa
                                        print(f'Soma dos dados é {dado[2]} * {aluguel(personagem[i][0])[0]} é = {soma_empresa}')
                                        print(f'{personagem[i][1]}, pagou R${soma_empresa} para {personagem[a][1]}')
                        elif pe == 2: # Você é o dono
                            print('Você é o dono')
# Verificação sorte ou revez        
                    elif lugar(personagem[i][0])[0] == 3:
                    # Sorte ou Revez
                        while True:
                            sorte = sorte_ou_revez()
                            if sorte[0] == 0: # Sorte
                                personagem[i][2] += sorte[2]
                                print(f'Sorte: {sorte[1]}, ganhou R${sorte[2]}')
                                break
                            elif sorte[0] == 1: # Azar
                                personagem[i][2] += (-sorte[2])
                                print(f'Azar: {sorte[1]}, perdeu R$-{sorte[2]}')
                                break
                            elif sorte[0] == 2: # Hábias corpus
                                print(traço1)
                                total_hábias = 0
                                for a in range(0,len(personagem)):
                                    if personagem[a][6] > 0:
                                        total_hábias += personagem[a][6]
                                if total_hábias <= 2:
                                    personagem[i][6] += 1
                                    break  
                            elif sorte[0] == 3: # Preso
                                print(traço1)
                                personagem[i][0] = 40
                                personagem[i][4] = quant_preso
                                print(f'Azar: {sorte[1]}')
                                break
# Verificação da cadeia
                    elif lugar(personagem[i][0])[0] == 4:
                    # Condição da prisão
                        print(traço1)
                        personagem[i][0] = 40
                        personagem[i][4] = quant_preso # Acrescenta mais, quantidade de rodada preso
                        print(f'{personagem[i][1]}, você foi preso!')
# Verificação do bonus
                    elif lugar(personagem[i][0])[0] == 5:
                        if lugar(personagem[i][0])[2] > 0: # Ganha dinheiro
                            personagem[i][2] += lugar(personagem[i][0])[2]
                            print(f'{personagem[i][1]}, ganhou R${lugar(personagem[i][0])[2]}')
                        elif lugar(personagem[i][0])[2] < 0: # Paga dinheiro
                            personagem[i][2] += lugar(personagem[i][0])[2]
                            print(f'{personagem[i][1]}l, pagou R${lugar(personagem[i][0])[2]}')
                    #print(traço1)
                    #print(personagem)
                    if rodada == total_rodada: # Determina o fim apos x de rodadas
                        break
                    if personagem[i][4] > 0: # Retira uma rodada por jogada
                        personagem[i][4] -= 1
                        if personagem[i][4] == 0:
                            print(traço1)
                            personagem[i][0] = 10
                            print(f'Fim da prisão')
                    rodada += 1
                    i += 1
# Final da logica do jogo
        elif menu_jogo == 2:
            while True:
                print(traço)
                menu0 = str(input('''Configuração
[ 0 ] Voltar
[ 1 ] Resetar jogo
[ 2 ] Total de rounds
[ 3 ] Jogadas automáticas
Digite aqui: '''))
                if menu0.isnumeric() == True:
                    menu0 = int(menu0)
                    if menu0 == 0:
                        break
                    elif menu0 == 1:
                        personagem = bkp_personagem
                        rodada = 1
                        i = 0
                        print(traço1)
                        print('Ficha resetada com sucesso')
                        break
                    elif menu0 == 2:
                        while True:
                            print(traço1)
                            config = str(input(f'''Total de rounds é {total_rodada}
[ 0 ] Voltar
digite a quantidade limite de rounds!: '''))
                            if config.isnumeric() == True:
                                config = int(config)
                                if config == 0:
                                    break
                                else:
                                    total_rodada = config
                                    print(traço1)
                                    print('Total de round atualizado')
                                    break
                    elif menu0 == 3:
                        while True:
                            print(traço1)
                            for a in range(0,len(personagem)):
                                if personagem[a][5] == 0: # Manual
                                    print(f'{personagem[a][1]}, está configurado como manual')
                                elif personagem[a][5] == 1: # Automático
                                    print(f'{personagem[a][1]}, está configurado como automático')
                            print(traço1)
                            config = str(input('''O que deseja fazer?
[ 0 ] Voltar
[ 1 ] Todas jogadores manual
[ 2 ] Todos jogadores automático
[ 3 ] Escolha individual
Digite aqui: '''))
                            if config.isnumeric() == True:
                                config = int(config)
                                if config == 0:
                                    break
                                elif config == 1:
                                    for a in range(0,len(personagem)):
                                        personagem[a][5] = 0
                                    print('Todos estão manual')
                                    break
                                elif config == 2:
                                    for a in range(0,len(personagem)):
                                        personagem[a][5] = 1
                                    print('Todos estão automático')
                                    break
                                elif config == 3:
                                    while True:
                                        print(traço1)
                                        for a in range(0,len(personagem)):
                                            if personagem[a][5] == 0: # Manual
                                                print(f'Nº{a + 1}, {personagem[a][1]}, está configurado como manual')
                                            elif personagem[a][5] == 1: # Automático
                                                print(f'Nº{a + 1}{personagem[a][1]}, está configurado como automático')
                                        automático1 = str(input('''[ 0 ] Sair
[ Nº ] Digite o número do personagem para ser alterado
Digite aqui: '''))
                                        if automático1.isnumeric() == True:
                                            automático1 = int(automático1)
                                            if automático1 >= 0 and automático1 <= len(personagem):
                                                if automático1 == 0:
                                                    break
                                                else:
                                                    if personagem[automático1 - 1][5] == 0:
                                                        personagem[automático1 - 1][5] = 1
                                                        print(f'{personagem[automático1 - 1][1]}, alterado para \"Automático\"')
                                                    elif personagem[automático1 - 1][5] == 1:
                                                        personagem[automático1 - 1][5] = 0
                                                        print(f'{personagem[automático1 - 1][1]}, alterado para \"Manual\"')
                                                    break
        elif menu_jogo == 3:
            while True:
                print(traço)
                menu1 = str(input('''Estatística
[ 0 ] Voltar
[ 1 ] Estatística real
[ 2 ] Compra de lotes/empresa
[ 3 ] Transferência de aluguel
Digite aqui: '''))
                if menu1.isnumeric() == True:
                    menu1 = int(menu1)
                    if menu1 == 0:
                        break
                    elif menu1 == 1:
                        print(traço1)
                        # nome, total de propriedades compradas, valor gasto na compra
                        # nome, pagou x de aluguel
                        # nome, valor máximo e mínimo de dinheiro
                    elif menu1 == 2:
                        print(traço)
                        menu1_0 = str(input('''Escolha uma opção
[ 1 ] Info de compra de terreno
[ 2 ] Info de compra de casas
Digite aqui: '''))
                        if menu1_0.isnumeric() == True:
                            menu1_0 = int(menu1_0)
                            if menu1_0 == 1:
                                print(traço1)
                                for a in compra_lote:
                                    print(a)
                                print(traço1)
                                print(f'Total de compra de lotes: {len(compra_lote)}')
                            elif menu1_0 == 2:
                                print(traço1)
                                for a in compra_casa:
                                    print(a)
                                print(traço1)
                                print(f'Total de compra de casas: {len(compra_casa)}')
                    elif menu1 == 3:
                        print(traço1)
                        for a in aluguel_jogador:
                            print(a)
                        print(traço1)
                        print(f'Total de transação: {len(aluguel_jogador)}')
            