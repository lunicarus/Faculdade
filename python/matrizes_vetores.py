def montaMatriz(M=0,N=0):
    matriz = []
    if M == 0 or N == 0:
        print("informe as dimensões da matriz (N,M)")
        N= int(input())
        M= int(input())

    for i in range(N):
        linha = []
        for j in range(M):
            elem = int(input(f"digite o elemento ({i},{j})"))
            linha.append(elem)
        matriz.append(linha)
    return matriz

def MaiorMenor(matriz):
        maior = matriz[0][0]
        menor = matriz[0][0]

        for linha in matriz:
            for elemento in linha:
                if elemento > maior:
                    maior = elemento
                if elemento < menor:
                    menor = elemento
        return f"maior : {maior} || menor : {menor}"

def montaMatrizT(matriz,n):
        matrizt = []
        for i in range(n):
            linha = []
            for j in range(n):
                linha.append(matriz[j][i])
            matrizt.append(linha)
        return matrizt
# [0,1,2]
# [0,2,3]
# [0,0,0]
##
def elementosNulos(matriz,n,m): 
        Lnulos = 0
        Cnulos = 0

        for linha in matriz: #[0,1,2] 
            if sum(linha) == 0:
                Lnulos +=1
        Lnulos = 0

        for j in range(n):
            soma_coluna = 0
        for i in range(m):
            soma_coluna += matriz[i][j]
        if soma_coluna == 0:
            Lnulos += 1
        
        print("Quantidade de linhas nulas: ", Lnulos)
        print("Quantidade de colunas nulas: ", Cnulos)
def produtomatriz(matriz1,matriz2,m,n,q):
        matrizp = []
        for i in range(m):
            linha = []
            for j in range(q):
                soma = 0
                for k in range(n):
                    soma += matriz1[i][k] * matriz2[k][j]
                linha.append(soma)
            matrizp.append(linha)
        print(f"Matriz 1: {matriz1}")
        print(f"Matriz 2: {matriz2}")
        print(f"Matriz Produto: {matrizp}")


        
            
            


def ex1():
    print(MaiorMenor(montaMatriz()))

def ex2():
    n=int(input("Informe a dimensão da matriz A quadrada: "))
    
    matriz= montaMatriz(n,n)
    matrizt= montaMatrizT(matriz,n)
    print(f"matriz: {matriz} \nmatrizT: {matrizt}")

def ex3():     
    n=int(input("Informe a dimensão da matriz A quadrada: "))
    matriz= montaMatriz(n,n)
    matrizt= montaMatrizT(matriz,n)
    print(f"matriz: {matriz} \nmatrizT: {matrizt}")
    if matriz==matrizt:
        print("A matriz é simetrica")
    else:
        print("Esta matriz não é simetrica")

def ex4():
    n= int(input())
    m= int(input())
    matriz= montaMatriz(n,m)
    elementosNulos(matriz,n,m)
def ex5():
    m = int(input("Digite a quantidade de linhas da matriz 1: "))
    n = int(input("Digite a quantidade de colunas da matriz 1: "))
    p = int(input("Digite a quantidade de linhas da matriz 2: "))
    q = int(input("Digite a quantidade de colunas da matriz 2: "))
    matriz1 = montaMatriz(m,n)
    matriz2 = montaMatriz(p,q)
    if n != p:
        print("Não é possível realizar a multiplicação das matrizes.")
    else:
        produtomatriz(matriz1,matriz2,m,n,q)
