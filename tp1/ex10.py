#Exercicio 10
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("------------------------------------------")
p1 = int(input("Digite o valor do 1º produto: R$"))
p2 = int(input("Digite o valor do 2º produto: R$"))
p3 = int(input("Digite o valor do 3º produto: R$"))
p4 = int(input("Digite o valor do 4º produto: R$"))
p5 = int(input("Digite o valor do 5º produto: R$"))
print("")
soma = p1 + p2 + p3 + p4 + p5
valor = int(input("digite o valor referente ao pagamento dos produtos: R$"))
resultado = valor - soma
print("")
print("O troco a ser devolvido é: R$"+str(resultado))
print("------------------------------------------")