'''
Exercício Fix21  
Faça um algoritmo com três variáveis numéricas (tipo int) que realize a média aritmética 
da multiplicação desses 3 valores. Mostre os resultados na tela. Os mesmos devem ser solicitados 
ao usuário, digite os valores via teclado. 
'''
#Exercicio 1
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("Média aritmética de 3 variáveis numéricas")

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

media = ((valor1*valor1)+(valor2*valor2)+(valor3*valor3))//3

print("O resultado da média aritmética é: "+str(media))
print("--------------------------------------------")