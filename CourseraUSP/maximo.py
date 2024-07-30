# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles. 


def maximo(a, b):
    if a > b:
        return a
    else:
        return b

# Teste da função
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

maior_numero = maximo(num1, num2)
print(maior_numero)
