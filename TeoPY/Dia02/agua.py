""" # Faça um programa que vende uma garrafa de água:
a. Se o cliente escolher água mineral natural, será cobrado R$1,50
b. Se o cliente escolher água mineral com gás, será cobrado R$2,50 """

preco = 0
escolha = input("Digite a caso queira água mineral natural e b caso queira água mineral com gás e digite a quantidade\n")
quantidade = int(input("digite a quantidade\n"))

if escolha == "a":
    preco = quantidade * 1.50
    print ("A agua mineral natural custa 1,50\n")

elif escolha == "b":
    preco = quantidade * 2.50
    print ("A água mineral com gás custa 2,50 \n")

else: 
        print ("Opção inválida, digite A ou B")

print ("O total é: ", preco)

