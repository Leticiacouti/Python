'''
Exercício Fix26  

Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões 
de 3,6 litros, que custam R$ 35,00. 

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
a) comprar apenas latas de 18 litros; 
b)	comprar apenas galões de 3,6 litros; 
c)	misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre 
arredonde os valores para cima, isto é, considere latas cheias.
'''

#Exercicio 6
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("Loja de tintas")
print("")

tamanho = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = tamanho / 6
litros_combinacao = (litros*10)/100
latas = litros // 18 + 1
galoes = litros //3.6 + 1
preco_latas = latas*80
preco_galoes = galoes*25
combinacao = (litros_combinacao//18)*80+((litros%18)//3.6+1)*25

print("O preço só com latas é: "+str(preco_latas))
print("O preço só com galões é: "+str(preco_galoes))
print("O preço com a combinação é: "+str(combinacao))
print("--------------------------------------------")