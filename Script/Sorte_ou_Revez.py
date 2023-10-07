def sorte_ou_revez():
    from random import randint
    
    # Sorte
    # Condição: 0-sorte, 1-azar, 2-hábias corpus, 3-prisão
    lista1 = [
        0,'Ganhou na loteria',30,
        0,'Achou dinheiro na rua',130,
        2,'Hábias corpus',0
    ]
    # Revez
    lista2 = [
        1,'Comprou uma geladeira nova',130,
        1,'Foi assaltado',20,
        3,'Foi preso',0
    ]
    
    lista = []
    lista.append(lista1)
    lista.append(lista2)
    x = randint(0,1) # Escolher se vai ser sorte ou azar
    quant = int(len(lista[x]) /3) - 1
    y = randint(0,quant)
    y = y * 3
    return lista[x][y], lista[x][y+1], lista[x][y+2]
