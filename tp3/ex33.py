'''
Exercício Fix33 
Altere o algoritmo anterior (Fix32) para que o usuário entre com a nota do exame. Lembre-se que 
deve se realizar a média aritmética entre a média e a nota do exame. O sistema deverá informar a 
ele as seguintes mensagens: 
a)	Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está aprovado. 
b)	Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o mínimo necessário. 
'''

#Exercicio 3
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

nome = input(("Digite o seu nome: "))
ra = input(("Digite o seu RA: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
exame = float(input("Digite a nota do exame: "))

media = (nota1+nota2)/2
media_final = (media+exame)/2

if(media_final >= 5):
    print("Parabéns, você aproveitou a sua chance! Está aprovado.")
else:
    print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")