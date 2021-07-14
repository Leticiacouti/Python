'''
Exercício Fix38 
Elabore um programa em Python  que o usuário entre com seu e seu salário. Se o salário for menor ou igual 
a R$1500,00 coloque um acréscimo de 20% de aumento. Se for maior que R$1500,00 e menor que R$2500,00 o 
acréscimo será de 10%, senão o acréscimo será de 5% para os demais valores. 
'''

#Exercicio 8
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
salario = float(input("Digite o seu salário: "))

if(salario <= 1500):
    resultado = ((20*salario)/100)+salario
    print("O seu salário com 20% de aumento é: "+str(resultado))
elif(salario > 1500 < 2500):
    resultado = ((10*salario)/100)+salario
    print("O seu salário com 10% de aumento é: "+str(resultado))
else:
    resultado = ((5*salario)/100)+salario
    print("O seu salário com 5% de aumento é: "+str(resultado))