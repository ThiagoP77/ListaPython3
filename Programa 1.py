"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 1. Faça um programa que peça uma nota, entre zero e
dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
Data: 15/10/21
"""
#Entrada de dados e processamento de dados
print("==========================")
print("PROGRAMA QUE VERIFICA NOTA")
print("==========================")
print(" ")
nota = float(input("Digite sua nota: "))#Comando que pede para o usuário inserir uma nota
print(" ")
while(nota<0)or(nota>10):#Comando que roda ao inserir nota inválida e exige que a nota esteja entre 0 e 10
    print("Nota inserida inválida!")
    nota = float(input("Digite uma nota entre 0 e 10: "))
    print(" ")
    
#Saída de dados
if(nota>=0)and(nota<=10):#Comando que gera o resultado para o usuário quando a nota é válida
    print("==========")
    print("RESULTADO!")
    print("==========")
    print(" ")
    print("Nota válida!")
