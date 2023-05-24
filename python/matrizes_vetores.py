def ex1():
    matriz=[]

    N=int(input("Informe a quantidade de linhas: "))
    M=int(input("Informe a quantidade de colunas: "))

    for i in range(N):
        linha=[]
        for j in range(M):
            elem=int(input(f"Digite o elemento da posição ({i},{j}): "))
            linha.append(elem)
        matriz.append(linha)
    maior=matriz[0][0]
    menor=matriz[0][0]

    for l in matriz:
        for elem in linha:
            if elem>maior:
                maior=elem
            if elem<menor:
                menor=elem
            
    print("O maior valor é: ", maior)
    print("O menor valor é: ", menor)
def ex2():
    matriz=[]
    n=int(input("Informe a dimensão da matriz A quadrada: "))
    for i in range(n):
        linha=[]
        for j in range(n):
            elem=int(input(f"Digite o elemento da posição ({i},{j}): "))
            linha.append(elem)
        matriz.append(linha)
    matrizt=[]
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(matriz[j][i])
        matrizt.append(linha)


    print("Matriz A:")
    for linha in matriz:
        print(linha)
    
    print("Matriz At:")
    for linha in matrizt:
        print(linha)
def ex3():     
    matriz=[]
    n=int(input("Informe a dimensão da matriz A quadrada: "))
    #criando a matriz original
    for i in range(n):
        linha=[]
        for j in range(n):
            elem=int(input(f"Digite o elemento da posição ({i},{j}): "))
            linha.append(elem)
        matriz.append(linha)
    
    matrizt=[]
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(matriz[j][i])
        matrizt.append(linha)


    print("Matriz A:")
    for linha in matriz:
        print(linha)
    
    print("Matriz At:")
    for linha in matrizt:
        print(linha)
    
    if matriz==matrizt:
        print("A matriz é simetrica")
    else:
        print("Esta matriz não é simetrica")
def ex4():
    a=[]


    n=int(input("Informe a quantidade de linhas: "))
    m=int(input("Informe a quantidade de colunas: "))


    for i in range(n):
        linha=[]
        for j in range(m):
            elem=int(input(f"Digite o elemento da posição ({i},{j}): "))
            linha.append(elem)
        a.append(linha)


    linnul=0
    for linha in a:
        if sum(linha)==0:
            linnul+=1


    colnul = 0
    for j in range(n):
        soma_coluna = 0
        for i in range(m):
            soma_coluna += a[i][j]
        if soma_coluna == 0:
            colnul += 1
        
    print("Quantidade de linhas nulas: ", linnul)
    print("Quantidade de colunas nulas: ", colnul)
def ex5():
    m = int(input("Digite a quantidade de linhas da matriz 1: "))
    n = int(input("Digite a quantidade de colunas da matriz 1: "))
    p = int(input("Digite a quantidade de linhas da matriz 2: "))
    q = int(input("Digite a quantidade de colunas da matriz 2: "))


    if n != p:
        print("Não é possível realizar a multiplicação das matrizes.")
    else:
        matriz1 = []
        for i in range(m):
            linha = []
            for j in range(n):
                elemento = int(input(f"Digite o elemento da posição ({i},{j}) da matriz 1: "))
                linha.append(elemento)
            matriz1.append(linha)


        matriz2 = []
        for i in range(p):
            linha = []
            for j in range(q):
                elemento = int(input(f"Digite o elemento da posição ({i},{j}) da matriz 2: "))
                linha.append(elemento)
            matriz2.append(linha)


        matrizp = []
        for i in range(m):
            linha = []
            for j in range(q):
                soma = 0
                for k in range(n):
                    soma += matriz1[i][k] * matriz2[k][j]
                linha.append(soma)
            matrizp.append(linha)


        print("Matriz 1:")
        for linha in matriz1:
            print(linha)
        print("Matriz 2:")
        for linha in matriz2:
            print(linha)
        print("Matriz Produto:")
        for linha in matrizp:
            print(linha)