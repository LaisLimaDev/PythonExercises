""" Faça um programa que receba o raio de
uma circunferência em centímetros. Retorne
para o usuário qual é a área e perímetro
desta circunferência no seguinte formato. """

raio = float(input("Digite o raio da circunferência: \n"))

import math

# Cálculo da área
area = math.pi * (raio ** 2)

# Cálculo do perímetro (circunferência)
perimetro = 2 * math.pi * raio

# Exibição dos resultados
print(f"A área do círculo é: {area:.2f}")
print(f"O perímetro do círculo é: {perimetro:.2f}")