# Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

def primeiros_impares(n):
    for i in range(n):
        print(2 * i + 1)

# Recebe um número inteiro positivo do usuário
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if n > 0:
    # Imprime os n primeiros números ímpares naturais
    primeiros_impares(n)
else:
    print("Por favor, digite um número inteiro positivo.")
