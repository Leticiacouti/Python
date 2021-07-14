'''
Exercício Fix31  
Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça: 
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado; 
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número;  
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9. 
'''

#Exercicio 1
import math
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
num = int(input("Escolha um número entre 1, 2, 3, 4, 6, 7, 8 ou 9: "))

if(num == 1):
    resultado = num ** 2
    print("O valor elevado ao quadrado é: "+str(resultado))
elif(num == 2):
    resultado = num ** 2
    print("O valor elevado ao quadrado é: "+str(resultado))
elif(num == 3):
    resultado = num ** 2    
    print("O valor elevado ao quadrado é: "+str(resultado))
elif(num == 4):
    resultado = math.sqrt(num)
    print("A raiz quadrada deste número é: "+str(resultado))
elif(num == 9):
    resultado = math.sqrt(num)
    print("A raiz quadrada deste número é: "+str(resultado))
elif(num == 6):
    resultado = num // 9
    print("O número dividido por 9 é: "+str(resultado))
elif(num == 7):
    resultado = num // 9
    print("O número dividido por 9 é: "+str(resultado))
elif(num == 8):
    resultado = num // 9
    print("O número dividido por 9 é: "+str(resultado))
else:
    print("Valor incorreto, tente novamente!")

