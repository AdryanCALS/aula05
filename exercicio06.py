cum = 0;cum2 = 0
for i in range(10):
    numeros = int(input("Digite os numeros: "))
    if numeros >= 10 and numeros <=20:
        cum +=1
    else:
        cum2 += 1
print(f"A quantidade de numeros no intervalo de [10--20] foi: {cum}, e a fora do intervalo foi: {cum2}")