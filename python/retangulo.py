
#imprime a primeira linha
print("*", end="")
for x in range(2,60):
    print("+", end="")
print("*")

#monta o meio
for y in range(1 , 9):
    print("+", end="")
    for x in range(2, 60):
        print(" ", end= "")
    print("+")
    
#imprime a ultima linha    
print("*", end="")
for x in range(2,60):
    print("+", end="")
print("*")