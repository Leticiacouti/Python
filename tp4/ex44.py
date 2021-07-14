'''
Exercício Fix44  
Desenvolva um programa para determinar a média geral do aluno. O mesmo deverá receber o nome do aluno,
as 2 notas obtidas do aluno nas 2 avaliações. Calcular a média de aproveitamento, usando a fórmula da
Media e escrever o conceito do aluno de acordo com a tabela de conceitos.

Média é dada pela fórmula: MG = (NP1*4 + NP2*6) / 10 

Tabela de atribuição de conceitos:  
Média de Aproveitamento 	Conceito 	SITUAÇÃO 
Nota entre  9,0 e 10 	       A 	    APROVADO 
Nota entre 7,0  e 9,0 	       B        APROVADO 
Nota entre  3,0  e 7,0 	       C 	    EXAME 
Nota entre  0,0 e menor        D        DP
que 3,0
 
Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois
faça um (print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo. 
'''

#Exercicio 4
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

nome = input("Digite seu nome: ")
NP1 = float(input("Digite a nota da NP1: "))
NP2 = float(input("Digite a nota da NP2: "))

MG = (NP1*4 + NP2*6) / 10

if(MG >= 9):
    print("Conceito: A")
    print("Situação: Aprovado")
elif(MG >= 7 <= 9):
    print("Conceito: B")
    print("Situação: Aprovado")
elif(MG >= 3 < 7):
    print("Conceito: C")
    print("Situação: Exame")
elif(MG >=0 < 3):
    print("Conceito: D")
    print("Situação: DP")
