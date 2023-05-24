

def ehinteiroP(n):
    
    try:
        i = int(float(n))
        f = float(n)
        if f < 0:
            print("numero negativo")
            return False
        elif i != f:
           print(n)
           return False
        else:
            print("numero flutuante")
            return True
        
    except:
        return False
    
def ehinteiro(n):
    
    try:
        i = int(float(n))
        f = float(n)
        if i != f:
           print(f"{n} não pode ser convertido pois é numero flutuante")
           return False
        else:
            print("numero inteiro")
            return True
        
    except:
        print("tipo de dados incompativel")
        return False

def ehReal(n):
    try:
        R = float(n)
        if type(R) != type(3.3):
            print("valor é integral")
            return False
        else:
            print(f"valor pode ser convertido: {R}")
            return True
    except:
        print("valor incompativel para conversão")
        return False
    
def funcPNZ(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

def notas(listaNotas):
    media = 0
    for nota in listaNotas:
        if ehReal(nota) == True:
            media += nota
        else:
            print("função recebeu valores incompativeis")
            return False
    return media/len(listaNotas)

def fatorial(n):
    if ehinteiroP(n) == True:
        P = n-1
        while P > 1:
            n = P*n
            P -=1
    return n

def uniao(l1,l2):
    uni = l1.copy()
    for n in l2:
        uni.append(n)
    
    return uni

def diferenca(l1,l2):
    dif = l1.copy()
    for n in l2:
        for m in dif:
            if n == m:
                dif.remove(m)
    return dif

def intersec(l1,l2):
    interc = []
    for n in l1:
        for m in l2:
            if n == m:
                interc.append(n)
    return interc

def UDI(l1,l2):
    print(f"U = {uniao(l1,l2)}")
    print(f"I ={intersec(l1,l2)}")
    print(f"D ={diferenca(l1,l2)}")

def main():
    print(ehinteiro("-11"))
    print(ehinteiroP("-11"))
    ehReal("11.5")
    L1 = [1,2,3,4,5,6,7]
    L2 = [4,5,6]
    print(notas([10.0,5.5,9.5,8.5]))
    print(fatorial(4))
    print(f"l1 = {L1}")
    print(f"l2 = {L2}")
    print(f"uniao = {uniao(L1,L2)}")
    print(f"diferença = {diferenca(L1,L2)}")
    print(f"intersecção = {intersec(L1,L2)}")
    UDI(L1,L2)

main()