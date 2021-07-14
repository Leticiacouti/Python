'''
Exercício Fix39 
O usuário deve digitar seu nome e sua idade. O sistema deverá informar as seguintes mensagens: 
Bem vindo NOME você é maior de idade. 
Bem vindo NOME você é menor de idade. 
Bem vindo NOME você é maior de 65 anos. 
'''

#Exercicio 9
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print("Bem vindo %s você é maior de idade."%nome)
elif(idade < 18):
    print("Bem vindo %s você é menor de idade."%nome)
elif (idade >= 65):
    print("Bem vindo %s você é maior de 65 anos."%nome)
else:
    print("Valor inválido!")