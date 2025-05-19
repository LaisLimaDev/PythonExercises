a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if ( a == b) and (b == c):
    print ("Triângulo Equilátero.")
elif ( a == b) or (b == c):
    print ("Triângulo Isósceles.")
elif ( a > b+c ) or (b > a+c) or (c > a+b):
    print ("Não é possível formar um triângulo. ")
else : 
    print ("Triângulo escaleno.")