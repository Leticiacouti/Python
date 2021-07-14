'''
Exercício Fix34 
Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça: 
(1)	se o valor for 1 e 2, mostre o valor elevado ao cubo;  
(2)	se o valor for múltiplo de 3 mostre o fatorial desse número;  
(3)	se o valor for os valores 4, 5, 7 ou 8, mostre o valor dividido 9. Caso não seja nenhum 
dos valores, informe como “valor inválido”. 
'''

#Exercicio 4
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
from math import factorial
num = int(input("Escolha um número inteiro: "))

if (num == 1 or num == 2):
    resultado = num * num * num
    print("O número elevado ao cubo é: "+str(resultado))
elif (num // 3):
    resultado = factorial(num)
    print("Este número é múltiplo de 3: "+str(resultado))
elif(num == 4 or num == 5 or num == 7 or num == 8):
    resultado = num / 9
    print("O número dividido por 9 é: "+str(resultado))
else:
    print("Valor incorreto, tente novamente!")
