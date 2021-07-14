'''
Exercício Fix24  
Faça um algoritmo com duas variáveis numéricas (tipo int) que realize as 4 operações básicas 
(soma, subtração, multiplicação e divisão), mostre os resultados na tela. 
Os mesmos devem ser solicitados ao usuário, digite os valores via teclado. 
'''

#Exercicio 4
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("4 operações básicas!")
print("")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("")
print("1 - Soma entre os dois números")
print("2 - Subtração entre os dois números")
print("3 - Multiplicação entre os dois números")
print("4 - Divisão entre os dois números")
print("")
opcao = input("Escolha uma opção: ")

if (opcao == '1'):
    resultado = num1 + num2
    print("O resultado dessa soma é: "+str(resultado))
elif (opcao == '2'):
    resultado = num1 - num2
    print("O resultado dessa subtração é: "+str(resultado))
elif (opcao == '3'):
    resultado = num1 * num2
    print("O resultado dessa multiplicação é: "+str(resultado))
elif (opcao == '4'):
    resultado = num1 // num2
    print("O resultado dessa divisão é: "+str(resultado))
else:
    print("Valor inválido, tente novamente!")