"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 5. Altere o programa anterior permitindo ao usuário informar as
populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
Data: 16/10/21
"""
#Entrada de dados
print("============================================================")
print("CALCULAR QUANDO A POPULAÇÃO DE UMA CIDADE ALCANÇA A DE OUTRA")
print("============================================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")

popA_inicial = int(input("Informe a população da primeira cidade: "))#Comando que pede para o usuário inserir a população da primeira cidade
if(popA_inicial<0):#Comando que pula um espaço quando a população for maior do que zero
    print(" ")
while(popA_inicial<0):#Comando que exige um valor positivo para a população da primeira cidade
    print("Informação inválida!")
    popA_inicial = int(input("Digite um número maior que 0: "))
    print(" ")

porcentagemA = float(input("Informe a taxa(porcentagem) de crescimento da primeira cidade: "))#Comando que pede para o usuário inserir a porcentagem de crescimento da população da primeira cidade

popB_inicial = int(input("Informe a população da segunda cidade: "))#Comando que pede para o usuário inserir a população da segunda cidade
if(popB_inicial<0):#Comando que pula um espaço quando a população for maior do que zero
    print(" ")
while(popB_inicial<0):#Comando que exige um valor positivo para a população da segunda cidade
    print("Informação inválida!")
    popA_inicial = int(input("Digite um número maior que 0: "))
    print(" ")

porcentagemB = float(input("Informe a taxa(porcentagem) de crescimento da segunda cidade: "))#Comando que pede para o usuário inserir a porcentagem de crescimento da população da segunda cidade

#Processamento de dados
taxaA = (porcentagemA/100)#Divide a porcentagem de crescimento da cidade 1 por 100
taxaB = (porcentagemB/100)#Divide a porcentagem de crescimento da cidade 2 por 100
popA = popA_inicial#Variável que recebe a população da cidade 1
popB = popB_inicial#Variável que recebe a população da cidade 2
anos = 0#Variável que representa os anos até uma população alcançar a outra

if(popA_inicial<popB_inicial):#Calcula o resultado quando a população A é menor que a B
    while(popA<popB):#Comando que realiza os cálculos até a população A alcançar B
        anos += 1#Soma 1 a váriavel ano para cada vez que o comando while se repete
        crescimentoA = (popA*taxaA)#Váriavel que representa o crescimento da população A
        popA += crescimentoA#Acrescenta o crescimento populacional a quantidade de habitantes de A
        crescimentoB = (popB*taxaB)#Váriavel que representa o crescimento da população B
        popB += crescimentoB#Acrescenta o crescimento populacional a quantidade de habitantes de B

elif(popB_inicial<popA_inicial):#Calcula o resultado quando a população B é menor que a A
    while(popB<popA):#Comando que realiza os cálculos até a população B alcançar A
        anos += 1#Soma 1 a váriavel ano para cada vez que o comando while se repete
        crescimentoB = (popB*taxaB)#Váriavel que representa o crescimento da população B
        popB += crescimentoB#Acrescenta o crescimento populacional a quantidade de habitantes de B
        crescimentoA = (popA*taxaA)#Váriavel que representa o crescimento da população A
        popA += crescimentoA#Acrescenta o crescimento populacional a quantidade de habitantes de A
        
#Saída de dados
if(popA_inicial==popB_inicial):#Comando que gera o resultado quando as duas populações são iguais
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("Essas cidades já possuem o mesmo número de habitantes!")

elif(popA_inicial<popB_inicial)and(taxaA<=taxaB):#Comando que gera resultado quando a população e a taxa de crescimento A são menores que as de B
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("A população da primeira cidade nunca alcançará a da segunda!")

elif(popB_inicial<popA_inicial)and(taxaB<=taxaA):#Comando que gera resultado quando a população e a taxa de crescimento B são menores que as de A
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("A população da segunda cidade nunca alcançará a da primeira!")

elif(popA_inicial<popB_inicial)and(taxaA>taxaB):#Comando que gera resultado quando a população de A é menor que B, mas sua taxa de crescimento é maior
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("A população da primeira cidade alcançará a da segunda em %d anos." %(anos))
    print("População da primeira cidade: Cerca de %d habitantes." %(popA))
    print("População da segunda cidade: Cerca de %d habitantes." %(popB))

elif(popB_inicial<popA_inicial)and(taxaB>taxaA):#Comando que gera resultado quando a população de B é menor que A, mas sua taxa de crescimento é maior
    print(" ")
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("A população da segunda cidade alcançará a da primeira em %d anos." %(anos))
    print("População da primeira cidade: Cerca de %d habitantes." %(popA))
    print("População da segunda cidade: Cerca de %d habitantes." %(popB))
