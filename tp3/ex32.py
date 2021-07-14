'''
Exercício Fix32  
Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, 
nota 1 e nota 2. O sistema deverá informar a ele as seguintes mensagens: 
a)	Se a média for maior ou igual a sete: Parabéns, você está aprovado! 
b)	Se a média for menor que sete: Você ainda tem uma chance! Estude mais para o exame. 
'''
#Exercicio 2
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

nome = input(("Digite o seu nome: "))
ra = input(("Digite o seu RA: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if(media >= 7):
    print("Parabéns, você está aprovado!")
else:
    print("Você ainda tem uma chance! Estude mais para o exame.")