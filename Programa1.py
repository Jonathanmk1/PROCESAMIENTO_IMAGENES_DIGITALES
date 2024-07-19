print("Hola mundo")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 8]
tupla = (4, 6, 6, 5)

for i in lista:
    print(i, end=" ")

print("\n")
for i in range(len(lista)):
    print(lista[i], end=" ")

m = [[0, 3], [2, 1]]
print(m)
for i in range(len(m)): 
   # print(m[i])
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
print(type(m))