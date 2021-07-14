'''
Exercício Fix37  
Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 
ou se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é divisível 
por nenhum desses valores. 
'''

#Exercicio 7
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

num = int(input("Digite um número inteiro: "))

if(num % 10 == 0):
    print("Este número é divisível por 10!")
elif (num % 5 == 0):
    print("Este número é divisível por 5!")
elif (num % 2 == 0):
    print("Este número é divisível por 2!")
else:
    print("Este número não é divisível por 10, 5 e nem 2.")