import math

def delta (a, b, c):
    return b**2-4*a*c

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


if delta(a, b, c) == 0: 
    raiz1 = (-b + math.sqrt(delta(a, b, c)))/2*a
    print(" A unica raiz é: ", raiz1)
else:
    if delta() <0:
        print("a equação não possui raizes reais")
    else: 
        raiz1 = (-b + math.sqrt(delta(a, b, c)))/2*a
        raiz2 = (-b - math.sqr(delta(a, b, c)))/2*a
        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)







