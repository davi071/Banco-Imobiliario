def lugar(x):
    # 0-neutro, 1-propriedade(casa), 2-propriedade(empresa), 3-sorte ou revez, 4-prisão, 5-bonus, 6-mensagem-prisão
    lista = [
        0,'Inicio',0, # 0
        1,'Bonito, Mato Grosso do Sul',120, # 1
        1,'Chapada dos Veadeiros, Goiás',130, # 2
        1,'Pantanal',150, # 3
        3,'Sorte ou revez',0, # 4
        1,'Pirenópolis, Goiás',165, # 5
        2,'Petrolífera',200, # 6
        5,'Receita federal',-200, # 7
        1,'Chapada Diamantina, Bahia',145, # 8
        1,'Fernando de Noronha, Pernambuco',140, # 9
        0,'Visitando a prisão',0, # 10
        1,'João Pessoa, Paraíba',180, # 11
        1,'São Miguel do Gostoso, Rio Grande do Norte',195, # 12
        3,'Sorte ou revez',0, # 13
        1,'Boipeba',160, # 14
        2,'Princesa do Sul',200, # 15
        1,'São Miguel dos Milagres, Alagoas',170, # 16
        1,'Jericoacoara, Ceará',180, # 17
        2,'Biogas',150, # 18
        1,'Península de Maraú, Bahia',200, # 19
        0,'Ferias com a familia',0, # 20
        1,'Maceió, Alagoas',210, # 21
        1,'Praia da Pipa, Rio Grande do Norte',210, # 22
        3,'Sorte ou revez',0, # 23
        1,'Porto de Galinhas, Pernambuco',230, # 24
        2,'Ferroviária',200, # 25
        1,'Lençóis Maranhenses, Maranhão',200, # 26
        3,'Sorte ou revez',0, # 27
        1,'Itacaré, Bahia',190, # 28
        2,'Amazing',150, # 29
        4,'Preso',0, # 30
        1,'Arraial d\'Ajuda, Bahia',230, # 31
        1,'Morro de São Paulo, Bahia',210, # 32
        5,'Loteira',400, # 33
        1,'Tamandaré, Pernambuco',280, # 34
        3,'Sorte ou revez',0, # 35
        1,'Maragogi, Alagoas',300, # 36
        1,'Aracaju, Sergipe',290, # 37
        2,'Rodoviária',150, # 38
        1,'Natal, Rio Grande do Norte',220, # 39
        6,'Prisão',0 # 40
    ]
    y = x * 3
    return lista[y], lista[y+1], lista[y+2]

def aluguel(x):
    # aluguel, 1 casa, 2 casa, 3 casa, 4 casa, hotel
    lista = (
        0,0,0,0,0,0, # 0
        15,58,110,230,360,450, # 1
        18,62,150,290,400,510, # 2
        16,50,135,256,384,490, # 3
        0,0,0,0,0,0, # 4
        
        18,68,120,250,386,479, # 5
        50,0,0,0,0,0, # 6
        0,0,0,0,0,0, # 7
        20,73,150,320,390,520, # 8
        23,80,210,399,480,590, # 9
        
        0,0,0,0,0,0, # 10
        31,159,327,400,490,550, # 11
        28,145,321,385,472,530, # 12
        0,0,0,0,0,0, # 13
        32,164,340,421,532,598, # 14
        
        50,0,0,0,0,0, # 15
        40,150,360,590,710,900, # 16
        38,143,290,540,680,800, # 17
        40,0,0,0,0,0, # 18
        36,128,250,500,610,730, # 19
        
        0,0,0,0,0,0, # 20
        2,22,56,90,120,250, # 21
        4,37,69,115,210,320, # 22

        0,0,0,0,0,0, # 23
        45,250,460,690,800,1300, # 24
        50,0,0,0,0,0, # 25
        60,320,640,830,1100,2400, # 26
        0,0,0,0,0,0, # 27
        50,290,500,730,930,1900, # 28
        
        40,0,0,0,0,0, # 29
        0,0,0,0,0,0, # 30
        98,755,1000,1834,2300,2821, # 31
        104,767,1200,1999,2545,2910, # 32
        0,0,0,0,0,0, # 33
        110,780,1600,2100,2700,3100, # 34
        
        0,0,0,0,0,0, # 35
        25,100,250,470,640,800, # 36
        20,87,206,452,595,740, # 37
        40,0,0,0,0,0, # 38
        18,70,175,437,577,677 # 39
    )
    y = x * 6
    
    return lista[y], lista[y+1], lista[y+2], lista[y+3], lista[y+4], lista[y+5]

def lugar1(x):
    #ggg = (1,2,3,5,8,9,11,12,14,16,17,19,21,22,24,26,28,31,32,34,36,37,39)
    # Grupo das propriedades
    a = (1,2,3) # 1
    b = (5,8,9) # 2
    c = (11,12,14) # 3
    d = (16,17,19) # 4
    e = (21,22) # 5
    f = (24,26,28) # 6
    g = (31,32,34) # 7
    h = (36,37,39) # 8