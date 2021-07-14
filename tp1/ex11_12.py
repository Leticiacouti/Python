#Exercicio 11 e 12
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
valor = float(input("Digite o Valor da bolsa: "))

print("1 - A vista com 10% de desconto")
print("2 - Parcelado em 1+2 vezes sem desconto")
print("3 - Dividido em 10 vezes com juros de 5% sobre o valor total")
opcao = input("Escolha a forma de pagamento: ")

if (opcao == '1'):
    resultado_desconto = (10*valor)/100
    print("O valor que deverá ser pago é: R$"+str(resultado_desconto))
elif (opcao == '2'):
    resultado_sem_desconto = valor/2
    print("O valor de cada parcela sem desconto é: R$"+str(resultado_sem_desconto))
elif (opcao == '3'):
    resultado_juros = (valor*0.05)/10
    print("O valor de cada parcela com juros de 5% é: R$"+str(resultado_juros))
else:
    print("Valor inválido, tente novamente!")



    