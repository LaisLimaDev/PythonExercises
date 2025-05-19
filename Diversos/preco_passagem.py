distancia = float(input("Digite a quantidade de quilômetros que deseja percorrer: "))

if distancia <= 200 :
    valor_corrida = (distancia*0.5)
else: 
    valor_corrida = (distancia*0.45)
print ("O valor da corrida de ", distancia, " quilômetros é de: ", valor_corrida , ".")