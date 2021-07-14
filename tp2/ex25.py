'''
Exercício Fix25  
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso (p) ideal, 
utilizando as seguintes fórmulas: 
Para homens: (72.7*h) - 58 
Para mulheres: (62.1*h) - 44.7
'''

#Exercicio 5
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("Calculo do peso ideial de homem e mulher")
print("")

h = float(input("Digite a sua altura: "))

opcao = input("Digite M se você for mulher ou H se você for homem: ").upper()
print("")

if(opcao == 'M'):
    resultado = (62.1*h) - 44.7
    print("Seu peso ideal é: %2.f"%(resultado))
elif(opcao == "H"):
    resultado = (72.7*h) - 58
    print("Seu peso ideal é: %2.f"%(resultado))
else:
    print("Opção inválida, tente novamente!")