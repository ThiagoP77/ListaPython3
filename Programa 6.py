"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 6. Faça um programa que imprima na tela os números de 1 a
20, um abaixo do outro. Depois modifique o programa para que ele
mostre os números um ao lado do outro.
Data: 16/10/21
"""
#Processamento e saída de dados
print("========================================")
print("PROGRAMA QUE MOSTRA OS NÚMEROS DE 1 A 20")
print("========================================")
print(" ")
print("Lista com os números um embaixo do outro:")
print(" ")
numero_inicial = 0#Variável que representa o número inicial
numero_final = 20#Variável que representa o número final
while(numero_inicial<numero_final):#Comando que se repete até que a variável "numero_inicial" maior ou igual à "numero_final"
    numero_inicial += 1#Comando que soma 1 à "numero_inicial"
    print(numero_inicial)#Comando que mostra os números

print(" ")
print("Lista com os números um ao lado do outro:")
print(" ")
numero_inicial2 = 0#Variável que representa o número inicial
while(numero_inicial2<numero_final):#Comando que se repete até que a variável "numero_inicial2" maior ou igual à "numero_final"
    numero_inicial2 += 1#Comando que soma 1 à "numero_inicial2"
    print(numero_inicial2, end=" ")#Comando que mostra as números e os coloca lado a lado
    
