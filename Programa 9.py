"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 9. Faça um programa que imprima na tela apenas os números
ímpares entre 1 e 50.
Data: 16/10/21
"""
#Processamento e saída de dados
print("===================================================")
print("PROGRAMA QUE MOSTRA OS NÚMEROS ÍMPARES ENTRE 1 E 50")
print("===================================================")
print(" ")
numero_inicial = 1#Variável que representa o número inicial da contagem
numero_final = 50#Variável que representa o número final da contagem
print("Lista com os números um embaixo do outro: ")
print(" ")
while (numero_inicial<numero_final):#Comando que se repete enquanto a variável "numero_inicial" for menor que "numero_final"
    print(numero_inicial)#Mostra a variável "número_inicial"
    numero_inicial += 2#Soma dois à variável "numero_inicial"

print(" ")
print("Lista com os números um ao lado do outro: ")
print(" ")
numero_inicial2 = 1#Variável que representa o número inicial da contagem
while (numero_inicial2<numero_final):#Comando que se repete enquanto a variável "numero_inicial2" for menor que "numero_final"
    print(numero_inicial2, end = " ")#Mostra a variável "número_inicial2" repetidas vezes na mesma linha
    numero_inicial2 += 2#Soma dois à variável "numero_inicial2"

