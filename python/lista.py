def multiplosDe3():
    lista3 = []
    for x in range(1,150):
        if x % 3 == 0:
            lista3.append(x)
    print(f"lista de multiplos 3: {lista3}")
def notas():
    notas = []
    n = 0
    media = 0
    print("programa de notas, digite uma nota inferior a 0 para encerrar")
    while n >= 0:
        n = round(float(input("digite uma nota: ")),2)
        if n < 0:
            break
        media  += n
        notas.append(n)

    print(f"notas: {notas} || media: {media/len(notas)}")

def SomaParMultImpar():
    seq = []
    soma = 0
    multi = 1
    n = int(input("escreva o numero de elementos: "))
    for x in range(0,n):
        num = int(input("escreva um numero: "))
        seq.append(num)
        if num % 2 != 0:
            multi *= num
        else:
            soma +=num
    print(f"Sequência Original: {seq} || Soma dos Pares : {soma}", end="")
    print(f" || Multiplicação dos Impares: {multi}")
def repeteNrepete():
    seq = []
    seqRep = []
    seqNRep = []
    N = int(input("digite os N elementos a serem fornecidos na Lista"))
    for x in range(N):
        num = int(input("escreva um numero: "))
        seq.append(num)
        # 1 1 2 2 3
    for number in range(N):
        for nun in range(N):
            if seq[number] == seq[nun] and number != nun:
                seqRep.append(seq[number])
                break;
            elif nun == N-1:
                seqNRep.append(seq[number])
            else:
                continue;
    print(f"lista repete: {seqRep} || lista não repete: {seqNRep}")