'''
Exercício Fix53 
Desenvolver um programa que determine a área de uma figura geométrica: retângulo, triangulo ou círculo. 
Para isto utilize 3 funções que calculam a área de um objeto enviando parâmetros para as funções conforme
a entrada do usuário e retornando o valor calculado da área de acordo com a escolha do usuário. 
No programa deve ter um menu de opções que fica dentro de um laço while, esta é uma forma bem eficiente de
para se criar um menu.
'''

#Exercicio 3
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

from time import sleep

def area_retangulo(b, h):
    area = b * h
    print("A área do retângulo é %.2f"%(area))
def area_triangulo(b, h):
    area = (b * h) / 2
    print("A área do triângulo é %.2f"%(area))
def area_circulo(r):
    area = 3.14 * (r ** 2)
    print("A área do círculo é %.2f"%(area))

print("Cálculo da Área de uma Figura Geométrica")
print("--------------------------------------------")

opcao = None

while (opcao != 4):
    print("[1] Área do Retângulo")
    print("[2] Área do Triângulo")
    print("[3] Área do Círculo")
    print("[4] Sair do Programa")
    print("--------------------------------------------")
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 1):
        b = float(input("Digite o valor da base do Retângulo: "))
        h = float(input("Digite o valor da altura do Retângulo: "))
        area_retangulo(b, h)
    elif(opcao == 2):
        b = float(input("Digite o valor da base do Triângulo: "))
        h = float(input("Digite o valor da altura do Triângulo: "))
        area_triangulo(b, h)
    elif(opcao == 3):
        r = float(input("Digite o valor do raio do Círculo: "))
        area_circulo(r)
    elif(opcao == 4):
        print("Aguarde, estamos finalizando o programa...")
    else:
        print("Opção Inválida! Tente novamente.")
    print("--------------------------------------------")
    sleep(3)

print("Fim do Programa!")
