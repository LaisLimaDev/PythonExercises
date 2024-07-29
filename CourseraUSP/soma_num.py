#   Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída
def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

# Recebe um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Calcula a soma dos dígitos do número
resultado = soma_digitos(abs(numero))  # abs() é usado para lidar com números negativos

# Imprime o resultado
print(resultado)

