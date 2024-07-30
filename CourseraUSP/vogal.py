# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(caractere):
    # Lista de vogais
    vogais = 'aeiouAEIOU'
    # Verifica se o caractere está na lista de vogais
    return caractere in vogais

