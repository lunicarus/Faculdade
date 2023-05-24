def ex1():
    n = int(input("defina o numero de participantes da pesquisa: "))
    i = 0
    arq = open("pesquisa.txt","w")
    print("digite as informações no segunte formato")
    print("sexo idade fumante(sim ou nao) Escolaridade")
    while(i<n):
        arq = open("pesquisa.txt","a")
        resp = "\n" + input()
        arq.write(resp)
        i += 1
        arq.close()
    arq = open("pesquisa.txt","r")
    print(arq.read())
    arq.close()
    fumantes = 0
    naofu = 0
    mulheres = 0
    homens = 0
    homensmenos40 = 0
    mulheresmais40 = 0

    arq = open("pesquisa.txt","r")
    lista = []
    i = 0
    while(i<n):
        linha = arq.readline()
        lista.append(linha.split())
        i += 1
    lista.pop(0)
    for sublista in range(len(lista)):
        if lista[sublista][2] == 'sim':
            fumantes +=1
        else:
            naofu += 1
            if lista[sublista][0] == "masculino" and int(lista[sublista][1]) < 40:
                homensmenos40 += 1
                

        if lista[sublista][0] == "feminino":
            mulheres += 1
            if lista[sublista][2] == 'sim' and int(lista[sublista][1]) > 40:
                mulheresmais40 += 1

        else:
            homens +=1
        
    print(f"percentual de fumantes em relação ao todo: {(fumantes/(naofu+fumantes))*100:.2f}%")
    print(f"percentual de homens não fumantes abaixo de 40: {(homensmenos40/homens)*100:.2f}%")
    print(f"percentual de mulheres fumantes acima de 40: {(mulheresmais40/mulheres)*100:.2f}%")


    print(lista)

def ex2():
    p = int(input("digite o numero de eleitores: "))
    arq = open("votos.txt","w")
    print("digite o codigo do candidato a prefeito (100,200,300,400,500): ")
    i = 0
    while(i<p):
        arq = open("votos.txt","a")
        resp = "\n" + input()
        arq.write(resp)
        i += 1
        arq.close()
    candidatos = [0,0,0,0,0,0]
    codigos=[100,200,300,400,500,"nullo"]
    arq = open("votos.txt","r")
    lista = []
    i = 0
    while(i<=p):
        linha = arq.readline()
        lista.append(linha.split())
        i += 1
    lista.pop(0)
    for sublista in range(len(lista)):
        if int(lista[sublista][0]) == 100:
            candidatos[0] += 1
        elif int(lista[sublista][0]) == 200:
            candidatos[1] += 1
        elif int(lista[sublista][0]) == 300:
                candidatos[2] += 1
        elif int(lista[sublista][0]) == 400:
                candidatos[3] += 1
        elif int(lista[sublista][0]) == 500:
                candidatos[4] += 1
        else:
                candidatos[5] += 1
    for candidato in range(len(codigos)):
         print(f"{codigos[candidato]}:{candidatos[candidato]}")