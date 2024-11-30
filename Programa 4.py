"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 4. Supondo que a população de um país A seja da ordem de 80000
habitantes com uma taxa anual de crescimento de 3% e que a população de B
seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários
para que a população do país
A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.
Data: 15/10/21
"""
#Processamento de dados
popA = 80000#Váriavel que representa a população de A
taxaA = 0.03#Váriavel que representa a taxa de crescimento de A
popB = 200000#Váriavel que representa a população de B
taxaB = 0.015#Váriavel que representa a taxa de crescimento de B
anos = 0#Váriavel que representa q quantidade de anos 
while(popA<popB):#Comando que calcula população e anos até que A alcance B
    crescimentoA = (popA*taxaA)#Váriavel que representa o crescimento da população A
    popA += crescimentoA#Acrescenta o crescimento populacional a quantidade de habitantes de A
    crescimentoB = (popB*taxaB)#Váriavel que representa o crescimento da população B
    popB += crescimentoB#Acrescenta o crescimento populacional a quantidade de habitantes de B
    anos +=1#Soma 1 a váriavel ano para cada vez que o comando while se repete
    
#Saída de dados
print("===========================================================")#Conjunto de comandos que mostram o resultado para o usuário
print("PROGRAMA QUE CALCULA QUANDO A POPULAÇÃO DE A ALCANÇA A DE B")
print("===========================================================")
print(" ")
print("Resultados:")
print(" ")
print("A população da cidade A alcança a de B em %d anos." %(anos))
print("População de A nesse ano: %d habitantes." %(popA))
print("População de B nesse ano: %d habitantes." %(popB))
