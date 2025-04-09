# for i in range(1,11):
#     print(i)
# i = 1
# while i <= 10:
#     print(i, end = " ")
#     i += 1
# for i in range(10,0,-1):
#     print(i, end=" ")
#Triangulo retangulo:
# for i in range(1,10):
#     for j in range(1,i):
#         print("*", end=" ")
#     print()
#triangulo retangulo
# for i in range(1,11):
#     for k in range(1,i):
#         print("*", end=" ")
#     print()
#triangulo numeros
# x = 0
# for i in range(0,5):
#     for j in range(0,i):
#         x += 1
#         print(x, end=" ")
#     x = 0
#     print()
#triangulo numeros ao contrarrio

x = 0
for i in range(0,5):
    for j in range(0,i):
        for k in range(0,i):
            print(" ", end="")
        x += 1
        print(x, end=" ")
    x = 0
    print()