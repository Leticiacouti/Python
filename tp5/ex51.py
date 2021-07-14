'''
Exercício Fix51  
Elabore um programa que solicite ao usuário três números diferentes e exiba o dobro do maior número.
Para fazer isso separe seu código em duas funções diferentes: Uma função para retornar o maior dos
três números e outra função para dobrar o número.
'''

#Exercicio 1
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("")

def maior_num (num1, num2, num3):
    resultado = None
    if num1 > num2 and num1 > num3:
        resultado = num1
        print("{} é o maior número!".format(resultado))
    elif num2 > num1 and num2 > num3:
        resultado = num2
        print("{} é o maior número!".format(resultado))
    else:
        resultado = num3
        print("{} é o maior número!".format(resultado))
    return resultado

def dobro_num (num):
    return num * 2

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
print("")

num = maior_num(num1, num2, num3)
print("O dobro de {} é:".format(num), dobro_num(num))