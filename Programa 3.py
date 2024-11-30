"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 3. Faça um programa que leia e valide as seguintes
informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';

Data: 15/10/21
"""
#Entrada e processamento de dados
print("=========================")
print("PROGRAMA QUE VALIDA DADOS")
print("=========================")
print(" ")
print("-Preencha com os dados exigidos abaixo-")
print(" ")

nome = str(input("Informe seu nome: "))#Comando que pede para o usuário digitar seu nome
if(len(nome)<=3):#Comando que pula uma linha quando o nome não tiver mais que três caracteres
    print(" ")
while(len(nome)<=3):#Comando que exige um nome com mais de três caracteres 
    print("Nome inválido!")
    nome = str(input("Digite um nome com mais do que três caracteres: "))
    print(" ")

idade = int(input("Informe sua idade: "))#Comando que pede para o usuário digitar sua idade
if(idade<0)or(idade>150):#Comando que pula uma linha quando a idade não estiver entre 0 e 150
    print(" ")
while(idade<0)or(idade>150):#Comando que exige uma idade entre 0 e 150 anos
    print("Idade inválida!")
    idade = int(input("Digite uma idade entre 0 e 150: "))
    print(" ")

salario = float(input("Informe seu salário: "))#Comando que pede para o usuário digitar seu salário
if(salario<=0):#Comando que pula uma linha quando o salário for menor que 0
    print(" ")
while(salario<=0):#Comando que exige uma salário maior que 0
    print("Salário inválido!")
    salario = float(input("Digite um salário maior do que 0: "))
    print(" ")

sexo = str(input("Informe seu sexo(utilize M ou F): "))#Comando que pede para o usuário digitar seu sexo
if(sexo!="M")and(sexo!="m")and(sexo!="F")and(sexo!="f"):#Comando que pula uma linha quando o sexo digitado é inválido
    print(" ")
while(sexo!="M")and(sexo!="m")and(sexo!="F")and(sexo!="f"):#Comando que exige que o usuário utilize os caracteres certos para informar seu sexo
    print("Sexo inválido!")
    sexo = str(input("Digite M ou F: "))
    print(" ")

estado_civil = str(input("Informe seu Estado Civil(utilize S, C, V ou D): "))#Comando que pede para o usuário digitar seu estado civil
print(" ")
while(estado_civil!="S")and(estado_civil!="s")and(estado_civil!="C")and(estado_civil!="c")and\
(estado_civil!="V")and(estado_civil!="v")and(estado_civil!="D")and(estado_civil!="d"):#Comando que exige que o usuário utilize os caracteres certos para informar seu estado civil
    print("Estado civil inválido!")
    estado_civil = str(input("Digite S, C, V ou D: "))
    print(" ")

if(sexo=="M")or(sexo=="m"):#Comando que calcula gênero e status quando o sexo é masculino
    genero = "Masculino."
    if(estado_civil=="S")or(estado_civil=="s"):#Gera o status quando o estado civil é solteiro
        status = "Solteiro."
    elif(estado_civil=="C")or(estado_civil=="c"):#Gera o status quando o estado civil é casado
        status = "Casado."
    elif(estado_civil=="V")or(estado_civil=="v"):#Gera o status quando o estado civil é viúvo
        status = "Viúvo."
    elif(estado_civil=="D")or(estado_civil=="d"):#Gera o status quando o estado civil é divorciado
        status = "Divorciado."
        
elif(sexo=="F")or(sexo=="f"):#Comando que calcula gênero e status quando o sexo é feminino
    genero = "Feminino."
    if(estado_civil=="S")or(estado_civil=="s"):#Gera o status quando o estado civil é solteiro
        status = "Solteira."
    elif(estado_civil=="C")or(estado_civil=="c"):#Gera o status quando o estado civil é casado
        status = "Casada."
    elif(estado_civil=="V")or(estado_civil=="v"):#Gera o status quando o estado civil é viúvo
        status = "Viúva."
    elif(estado_civil=="D")or(estado_civil=="d"):#Gera o status quando o estado civil é divorciado
        status = "Divorciada."    

#Saída de dados
print("==========")#Conjunto de comando que gera o resultado quando as informações estão válidas
print("RESULTADOS")
print("==========")
print(" ")
print("Informações válidas!")
print(" ")
print("Nome: %s." %(nome))
print("Idade: %d." %(idade))
print("Salário: R$%.2f." %(salario))
print("Sexo: %s" %(genero))
print("Estado Civil: %s" %(status))
        
