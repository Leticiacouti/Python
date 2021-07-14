'''
Exercício Fix50  
Elabore um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem: 
“{nome} possui {idade} anos.”. Esta mensagem deve ser escrita em uma função. 
'''

#Exercicio 0
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("")

def nome_idade (nome,idade):
    print("{} possui {} anos.".format(nome,idade))

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
print("")

nome_idade(nome,idade)