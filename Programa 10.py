"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 10. Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo compreendido por eles.
Data: 16/10/21
"""
#Entrada de dados
print("=================================================")
print("PROGRAMA QUE MOSTRA INTERVALO DE NÚMEROS INTEIROS")
print("=================================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
numero_inicial = int(input("Informe o número inicial do intervalo: "))#Comando que pede ao usuário o primeiro número do intervalo
numero_final = int(input("Informe o número final do intervalo: "))#Comando que pede ao usuário o último número do intervalo
if(numero_final<=numero_inicial):#Comando que pula uma linha quando o número final for menor que o inicial
    print(" ")
while(numero_final<=numero_inicial):#Comando que exige um número final maior que o inicial
    print("Informações inválidas!")
    numero_final = int(input("Digite um número final maior que o inicial: "))#Comando que pede ao usuário o último número do intervalo
    print(" ")
print(" ")

#Processamento e saída de dados
numero_inicial2 = numero_inicial#Varável que recebe o número inicial do intervalo
print("==========")
print("RESULTADOS")
print("==========")
print(" ")
print("Lista com os números um embaixo do outro:")
print(" ")
while(numero_inicial<=numero_final):#Comando que se repte até que a variável "numero_inicial" seja maior que "numero_final"
    print(numero_inicial)#Comando que mostra a variável "numero_inicial"
    numero_inicial += 1#Comando que soma um à variável "numero_inicial"
    
print(" ")
print("Lista com os números um ao lado do outro: ")
print(" ")
while(numero_inicial2<=numero_final):#Comando que se repte até que a variável "numero_inicial2" seja maior que "numero_final"
    print(numero_inicial2, end = " ")#Comando que mostra a variável "numero_inicial2" na mesma linha várias vezes
    numero_inicial2 += 1#Comando que soma um à variável "numero_inicial2"
