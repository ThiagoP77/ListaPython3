"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 8. Faça um programa que leia 5 números e informe a soma e a
média dos números.
Data: 16/10/21
"""
#Entrada e processamento de dados
print("============================================")
print("CALCULADORA DE SOMA E MÉDIA DE CINCO NÚMEROS")
print("============================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
w = 0#Variável que representa o número de vezes que o comando while se repete
soma_numeros = 0#Varável que vai receber a soma dos números
while(w<5):#Comando que se repete até obter os cincos números e verifica o maior deles
    w += 1#Soma um à variável que representa o número de repetições
    if(w == 1):#Determina a variável "ordem" na primeira repetição
        ordem = "primeiro"
    elif(w == 2):#Determina a variável "ordem" na segunda repetição
        ordem = "segundo"
    elif(w == 3):#Determina a variável "ordem" na terceira repetição
        ordem = "terceiro"
    elif(w == 4):#Determina a variável "ordem" na quarta repetição
        ordem = "quarto"
    elif(w == 5):#Determina a variável "ordem" na quinta repetição
        ordem = "quinto"
    numero_informado = float(input("Informe o %s número: " %(ordem)))#Comando que pede para o usuário digitar um número
    soma_numeros += numero_informado#Comando que adiciona o número informado à variável soma

media_numeros = (soma_numeros/5)#Comando que calcula a média dos cinco números

#Saída de dados
print(" ")
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
if(soma_numeros%1==0):#Comando que mostra a soma dos números quando é inteira
    print("A soma dos cinco números é %d." %(soma_numeros))
else:#Comando que mostra a soma dos números quando não é inteira
    print("A soma dos cinco números é %.2f." %(soma_numeros))
if(media_numeros%1==0):#Comando que mostra a média dos números quando é inteira
    print("A média dos cinco números é %d." %(media_numeros))
else:#Comando que mostra a média dos números quando não é inteira
    print("A média dos cinco números é %.2f." %(media_numeros))
    
