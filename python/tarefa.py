def divpor7():
    # 1 a 100 inclusivo ou exclusivo??
    for x in range(1,101): #tomei como inclusivo
        if x % 7 == 0:  
            print(f"{x}")
        else:
            continue;

def divpor3e7():
    for x in range(1,101):
        if x % 3 == 0 and x % 7 == 0:
            print(f"{x}")
        else:
            continue;

def tabuada3():
    for x in range(1,10):
            print(f"{x} x 3 == {x*3}")

def tabuada():
    #1 a 10 inclusivo ou exclusivo??
    for x in range(1,11):
        print("\n")
        for y in range(1,11):
            print(f"{x} x {y} = {x*y}")

def primo():
    numero = int(input("escreva um numero"))
    for x in range(2,numero): 
        if numero % x == 0: 
            print("não é primo")
            return 0;
        else:
            continue;
    print("é primo")

def exponenciacao():
    numero =  int(input("escreva um numero"))
    expo =  int(input("escreva um exponencial"))
    total = numero
    x = 1
    while(expo > x):
        total = total * numero
        x +=1
    print(f"{numero} ^ {expo} == {total}")

def notas():
    notas4,notas6,restante = (0,0,0)
    nota = 0 
    while (nota >= 0):
        nota = round(float(input("digite uma nota")),2)
        if nota < 0:
            print(f"notas <= 4: {notas4}\nnotas maiores que 4 e menores que 6: {restante}\nnotas maiores que 6: {notas6}")
            print("programa encerrado!")
            break
        else:
            if nota < 4:
                notas4 +=1
            elif nota >= 6:
                notas6 +=1
            else:
                restante +=1
        
def fibo8():
    numero1 = 0
    numero2 = 1
    for x in range(8):
        print(numero1)
        numeo3 = numero1 + numero2
        numero1 = numero2
        numero2 = numeo3

def serie():
    n = int(input("digite N:"))
    total = 1
    print("S = 1",end= " ")
    primo = 3
    cont = 2
    while(cont <= n):
        for i in range(2,primo+1): # 2 3 4 5
            if i == primo: # 2 3 5
                print(f" {cont}/{primo} " , end="")
                total += (cont/primo)
                cont += 1 # 3
                primo += 1 # 4 5
                continue
            elif primo % i != 0:
                continue
            else:
                primo +=1
    print(f"|| S == {total:.3f}",end="")
        
def fatorial():
    numero = int(input("digite um numero"))
    for x in range(1,numero):
        numero *= x
    print(f"fatorial do numero fornecido: {numero}")     