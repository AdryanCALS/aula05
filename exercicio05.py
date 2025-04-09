cum = 0
for i in range(1,11):
    val = int(input("Digite um numero: "))
    if val < 0:
        cum +=1
print(f"Voce digitou {cum} numeros negativos!")