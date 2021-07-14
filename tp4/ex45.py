'''
Exercício Fix45  
Desenvolva um programa que só permita o acesso a pessoas autorizadas (professor, via autenticação)
para posteriormente realizar a média do aluno.  Para isto Considere o programa criado no Fix44. 

Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final,
depois faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo. 
'''

#Exercicio 5
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

cargo = input("Digite seu cargo: ").upper()
usuario = input("Digite seu nome de usuario: ").upper()
senha = input("Digite sua senha: ").upper()
print("")

if(cargo == "PROFESSOR" and usuario == "MEDINA" and senha == "1234"):
    nome = input("Digite o nome do aluno: ")
    NP1 = float(input("Digite a nota da NP1: "))
    NP2 = float(input("Digite a nota da NP2: "))
    print("")

    MG = (NP1*4 + NP2*6) / 10

    if(MG >= 9):
        print("Conceito: A")
        print("Situação: Aprovado")
    elif(MG >= 7 and MG <= 9):
        print("Conceito: B")
        print("Situação: Aprovado")
    elif(MG >= 3 and MG < 7):
        print("Conceito: C")
        print("Situação: Exame")
    elif(MG >=0 and MG < 3):
        print("Conceito: D")
        print("Situação: DP")
else:
    print("Autenticação Inválida!")