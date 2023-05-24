

# 

M = 3
N = 2
total = 1
num = int(input("digite um numero: "))
print("S = ", end= "")
for i in range(1,num):
    print(f" {N}/{M}",end="")
    total = total +  N/M
    M = M + 2
    N = N + 1
print(f"\nS = {total}")



    