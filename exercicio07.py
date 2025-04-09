cont = 0
for i in range(0,5):
    valores = int(input(f"Digite os valores({i}): "))
    cont = cont + valores
media = cont/5
print(f"A media entre os numeros digitados foi de: {media}")