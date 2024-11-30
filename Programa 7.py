"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 7. Faça um programa que leia 5 números e informe o
maior número.
Data: 16/10/21
"""
#Entrada e processamento de dados
print("==================================================")
print("PROGRAMA QUE ENCONTRA O MAIOR DENTRE CINCO NÚMEROS")
print("==================================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
w = 0#Variável que representa o número de vezes que o comando while se repete
maior_numero = 0#Varável que vai receber o maior número
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
    if(numero_informado>maior_numero):#Comando que verifica se o número digitado é maior que os anteriores e, caso for, redefine a variável do maior número
        maior_numero = numero_informado

#Saída de dados
if(maior_numero%1==0):#Comando que gera o resultado quando o maior número é inteiro
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("O maior dentre os cinco números digitados é o %d." %(maior_numero))

else:#Comando que gera o resultado quando o maior número não é inteiro
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("O maior dentre os cinco números digitados é o %.2f." %(maior_numero))
