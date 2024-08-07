
# Aula 1 curso de PY para DS canal "Teo mw why" usando VS Code, Anaconda e Jupyter


# Comentar 
# # %%

print("A")
print ("B")

# %%

# Início do uso do prompt interativo no vscode usando o "# %%"




# Para identificar o tipo da variável utilizamos o operador "type"
# ex: int
type (6)

# ex: float
type (7.2)


# Resto da divisão usamos o operador %

print (7%3)

# Parte inteira da divisão usamos //

print (7//3)

# Exponenciação utiliza-se **

print(10**2)
print (40**20)

# Aula 2

# Entrada de dados

x = input("Digite x: \n")
print (x)

# %% o input irá ler em formato de texto, para ler outros formatos e necessário converter o formato. Ex:

quebrado = float(input("Digite o número: \n"))
print (quebrado)

# Para arredondar uma saída numérica podemos usar a função round "round(nome da variavel, numerodesignificativos)"



# Quebra de linha utiliza o \n
# %%


# O input pode ser usado para interromper um programa ao dar enter

""" Atalhos: 
Ctrl + A: selecionAR O TEXTO INTEIRO
SHIFT + ALT + I : SELECIONARÁ TODAS AS LINHAS E COLOCARÁ O CURSOR NO FINAL DE CADA PALAVRA
SHIFT + HOME: IRÁ MANTER O TEXTO SELECIONADO E MOVER O CURSOR PARA O INÍCIO DE CADA LINHA
ABRIR PARÊNTESES + ABRIR aspas duplas + Home: cursor irá para o começo da linha 
Em seguida digitar print, teclar end (cursor irá para o início da linha), dar enter e digitar 
input() (DESSA forma cada linha irá ter o comando para dar enter) 
ctrl + F: localizar palavra (no pop-up terá opção para substituir todas da seleção) """

""" Selecionar a palavra/bloco, Ctrl + Shift + P + digitar UPPER: Deixar em caixa alta """


# A convenção de identação do python prevê o uso de 4 espaços




# Raiz quadrada via linha de comando

print(100**0.5)
print(300**(1/2))


# Aula 3

# Tanto digitar var = var + x ou var += x tem a mesma função de sobreescrever a variável

# Dividir em partes

# Estrutura lógica "in" permite verificar se determinada palavra está em um trecho. Ex: 

# %%

nome = "Téo Calvo"

print("Calvo" in nome)


# %%
