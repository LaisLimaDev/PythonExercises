palavra = str(input("Digite uma palavra "))


# método para tornar todas as palavras minúsculas : 

palavra_formatada = palavra.lower()


# método para inverter as palavras : 

inverter = palavra_formatada [::-1]

if inverter == palavra_formatada : 
    print (palavra, " é um palíndromo.")
else: 
    print (palavra, " não é um palíndromo.")
