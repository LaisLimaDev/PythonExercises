import math

# Entrada dos coeficientes a, b, e c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Cálculo do discriminante
delta = b**2 - 4*a*c

# Verificação das condições do delta
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    print("A única raiz é:", raiz1)
elif delta < 0:
    print("A equação não possui raízes reais")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("A primeira raiz é:", raiz1)
    print("A segunda raiz é:", raiz2)
