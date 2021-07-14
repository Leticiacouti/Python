'''
Exercício Fix52 
Elaborar um programa que determine o cálculo do salário e retorna o valor a ser pago
conforme o número de horas trabalhadas. Lembrando que as mesmas serão digitadas. 
Seguem as regras de negocio:
- Caso a quantidade de horas trabalhadas é menor ou igual a 40, o valor do salario é
apenas multiplicando a quantidade de horas pelo valor de cada hora trabalhada. 
- Caso o trabalhar tenha horas extras, é adicionado ao salário um valor pelas horas extras. 
 
Dica utilizar a função calcular_pagamento (HT, VH)
'''

#Exercicio 2
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("")

def calcular_pagamento(ht, vh):
    if(ht <= 40):
        salario_final = ht * vh
        print("O seu salário é de {} reais.".format(salario_final))
    elif(ht > 40):
        salario = ht * vh
        he = ht - 40
        horas_total = vh * he
        adicional = horas_total + (50/100)
        salario_final = salario + adicional
        print("O seu salário é de {} reais.".format(salario_final))
    
ht = float(input("Digite o total de horas trabalhadas: "))
vh = float(input("Digite o valor por hora: "))
print("")

calcular_pagamento(ht, vh)
