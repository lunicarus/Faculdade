def somaSec():
    sec0 = [[],[]]
    N = int(input("digite os N elementos a serem fornecidos em cada Lista"))
    soma = [0] * N
    for secs in sec0:
        for x in range(N):
            secs.append(int(input(f"digite um numero da sequencia {sec0.index(secs)}: ")))
            soma[x] = secs[x] + soma[x]
    print(f"sequencia 1: {sec0[0]} || sequencia 2: {sec0[1]} || soma : {soma}")

def seqCube():
    seq =[]
    seq3 = []
    N = int(input("digite os N elementos a serem fornecidos na Lista"))
    for x in range(N):
        seq.append(int(input(f"digite o elemento [{x}] da sequencia: ")))
        seq3.append(seq[x]**3)
    print(f"sequencia: {seq} || sequencia³ = {seq3}")

def seqInvert():
    #tem função pra isso, mas vou fazer no pelo pra vc não dizer que eu não estou praticando logica

    seq = []
    
    N = int(input("digite os N elementos a serem fornecidos na Lista"))
    for x in range(N):
        seq.append(int(input(f"digite o elemento [{x}] da sequencia: ")))
    qes = [0] * N
    for x in range(N):
        qes[x] = seq[-(x+1)]
    print(f"sequencia: {seq} || aicneuqes = {qes}")

def seqImparPar():
    seq = []
    seqAlter = []
    N = int(input("digite os N elementos a serem fornecidos na Lista"))
    for x in range(N):
        seq.append(int(input(f"digite o elemento [{x}] da sequencia: ")))
        if seq[x] % 2 == 0:
            seqAlter.append(1)
        else:
            seqAlter.append(-1)
    print(f"sequencia original: {seq} || sequencia alterada : {seqAlter}")