#Exercicio 14
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

quilo = 23 * 1000
peso_prato = 200 / 1000
prato_cliente = float(input("Digite o valor em quilos do prato: "))
valor = ((prato_cliente - peso_prato)*quilo)/1000

print("O valor a pagar é: R$"+str(valor))