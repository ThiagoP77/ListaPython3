"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 2. Faça um programa que leia um nome de usuário
e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
Data: 15/10/21
"""
#Entrada de dados
print("===========================")
print("PROGRAMA QUE VERIFICA SENHA")
print("===========================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
nome = str(input("Digite seu nome: "))#Comando que pede para o usuário inserir seu nome
senha = str(input("Digite sua senha: "))#Comando que pede para o usuário inserir sua senha
print(" ")

#Processamento de dados
while(nome==senha):#Comando que pede o nome e senha até que sejam diferentes
    print("Informações inválidas!")
    nome = str(input("Digite seu nome: "))
    senha = str(input("Digite uma senha que seja diferente do seu nome: "))
    print(" ")
    
#Saída de dados
if(senha!=nome):#Comando que gera o resultado quando nome e senha são diferentes
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Informações válidas!")
