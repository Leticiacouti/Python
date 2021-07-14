'''
Exercício Fix23  
Faça um algoritmo que mostre os descontos concedidos pela loja ABC em suas mercadorias. 
Em compras acima de 300,00 forneça 20% de desconto, para 200,00 desconto de 15% e acima de 100,00 
o desconto será de 10%. Atribua valores as variáveis compra1, compra2 e compra3. Mostre na tela o 
valor total e o valor com o devido desconto. Os mesmos devem ser solicitados ao usuário, digite os 
valores via teclado.
'''

#Exercicio 3
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

compra1 = float(input("Digite o preço da primeira compra: "))
compra2 = float(input("Digite o preço da segunda compra: "))
compra3 = float(input("Digite o preço da terceira compra: "))
print("")

if(compra1 >= 300):
    print("O valor total da 1º compra é: R$"+str(compra1))
    resultado_1 = (20*compra1)/100
    print("O valor com desconto da 1º compra é: R$%.2f"%(resultado_1))
elif (compra1 >= 200):
    print("O valor total da 1º compra é: R$"+str(compra1))
    resultado_2 = (15*compra1)/100
    print("O valor com desconto da 1º compra é: R$%.2f"%(resultado_2))
elif (compra1 >= 100):
    print("O valor total da 1º compra é: R$"+str(compra1))
    resultado_3 = (10*compra1)/100
    print("O valor com desconto da 1º compra é: R$%.2f"%(resultado_3))
else:
    print("Você não conseguiu desconto, o valor total da 1º compra é: R$"+str(compra1))

print("")

if(compra2 >= 300):
    print("O valor total da 2º compra é: R$"+str(compra1))
    resultado_1 = (20*compra2)/100
    print("O valor com desconto da 2º compra é: R$%.2f"%(resultado_1))
elif (compra2 >= 200):
    print("O valor total da 2º compra é: R$"+str(compra1))
    resultado_2 = (15*compra2)/100
    print("O valor com desconto da 2º compra é: R$%.2f"%(resultado_2))
elif (compra2 >= 100):
    print("O valor total da 2º compra é: R$"+str(compra1))
    resultado_3 = (10*compra2)/100
    print("O valor com desconto da 2º compra é: R$%.2f"%(resultado_3))
else:
    print("Você não conseguiu desconto, o valor total da 2º compra é: R$"+str(compra2))

print("")

if(compra3 >= 300):
    print("O valor total da 3º compra é: R$"+str(compra3))
    resultado_1 = (20*compra3)/100
    print("O valor com desconto da 3º compra é: R$%.2f"%(resultado_1))
elif (compra1 >= 200):
    print("O valor total da 3º compra é: R$"+str(compra3))
    resultado_2 = (15*compra3)/100
    print("O valor com desconto da 3º compra é: R$%.2f"%(resultado_2))
elif (compra1 >= 100):
    print("O valor total da 3º compra é: R$"+str(compra3))
    resultado_3 = (10*compra3)/100
    print("O valor com desconto da 3º compra é: R$%.2f"%(resultado_3))
else:
    print("Você não conseguiu desconto, o valor total da 3º compra é: R$"+str(compra3))