# Escreva um programa que receba um número natural nn na entrada e imprima n!n! (fatorial) na saída.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Recebe um número natural n do usuário
n = int(input("Digite o valor de n:"))

# Calcula o fatorial de n
resultado = fatorial(n)

# Imprime o resultado
print(resultado)
