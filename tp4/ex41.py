'''
Exercício Fix41 
Elaborar um algoritmo (programa) que calcule o valor fatorial de um número inteiro positivo. 
Utilize a estrutura de controle  for ...in .  
Cálculo do fatorial, exemplo: fatorial de 5 = 5!=1x2x3x4x5= 120 
'''

#Exercicio 1
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("Calculo de um valor fatorial de um número inteiro positivo")

numero = int(input("Fatorial de: ") )

resultado = 1
for n in range(1,numero+1):
    resultado *= n

print(resultado)