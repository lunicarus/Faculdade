def formula():
    emprestimo = 150000
    saldo_inicial = 150000
    saldo_final = saldo_inicial
    #J = P * (1 + i)^n - P
    #VF = P * (1 + i)^n
    

    for ano in range(1,10):
        saldo_final = saldo_inicial * pow((1+0.02),ano) 
        juros = saldo_final - saldo_inicial
        print(f"saldo inicial no ano{ano}: {saldo_inicial} ||", end=" ")
        
        print(f"juros={juros} || saldo final:{saldo_final} || crescimento = {emprestimo/saldo_final:.2f}")
        saldo_inicial = saldo_final
formula()