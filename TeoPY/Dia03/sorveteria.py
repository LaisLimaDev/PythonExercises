""" Ex 3 

Faça o programa de uma sorveteria, onde o usuário pode escolher:
a. Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
b. Sabor do sorvete: morango, creme, chocolate
c. Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem
cobertura (R$0,00)
Apresente o valor a ser pago """


print ("Tipo de sorvete 1 - casquinha (R$1,00)\n")
print ("Tipo de sorvete 2 - cascão (R$2,50)\n ")
print ("Tipo de sorvete 3 - cestinha (R$4,00)\n ")
print ("Sabor do sorvete: morango, creme, chocolate\n ")
print ("Cobertura 1: Caramelo (R$1,50)\n  ")
print ("Cobertura 2: morango (R$1,50)\n ")
print ("Cobertura 3: chocolate (R$1,50)\n ")
print ("4 - sem cobertura (R$0,00)\n ")
tipo = input("Digite o tipo de sorvete\n")
sabor = input("Digite o sabor\n")
cobertura = input("Digite o número do tipo de cobertura desejado\n")


valortipo =  0

preco =  0

valorcobertura =  0 

if tipo == "casquinha":
    valortipo = 1.00
elif tipo == "cascão":
    valortipo =  2.50
elif tipo == "cestinha":
    valortipo = 4.00
else: 
    print ("Digite a opção correspondente ao tipo de sorvete desejado")

if cobertura == "caramelo" or cobertura == "morango" or cobertura == "chocolate":
    valorcobertura = 1.50
elif cobertura == "sem cobertura": 
    valorcobertura = 0
else: 
    print("Digite a opção da cobertura desejada")


preco = valortipo + valorcobertura

print = ("O total do sorvete ", tipo, "sabor ", sabor, " com cobertura ", cobertura, " fica: R$", preco)
