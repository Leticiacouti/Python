'''
Exercício Fix36 
Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça: 
(1)	se for um valor negativo, mostre o módulo (valor sem sinal) do valor; 
(2)	se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles; 
(3)	Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5 
'''

#Exercicio 6
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

num = float(input("Digite um número: "))

if(num < 0):
    resultado = abs(num)
    print("O módulo do número é: "+str(resultado))
elif(num > 10):
    num2 = float(input("Digite outro número: "))
    resultado = num - num2
    print("A diferença entre esses dois números é: "+str(resultado))
else:
    resultado = num / 5
    print("O número dividido por 5 é: "+str(resultado)) 