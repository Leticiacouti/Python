'''
Exercício Fix35 
Elabore um programa em PYTHON, que mostre os descontos concedidos pela loja ABC em suas mercadorias.  
Em compras acima de R$ 300,00 forneça 20% de desconto, entre R$ 200,00 a R$ 299,99 desconto de 10% e 
abaixo de R$ 199,99 o desconto será de 5%.  
Mostre na tela o valor total e o valor final a pagar (com o desconto).  Solicite ao usuário que digite 
os valores via teclado. 
'''

#Exercicio 5
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("Loja ABC")
print("")

preco = float(input("Digite o valor da compra: "))

if(preco > 300):
    resultado = (20*preco)/100
    print("O seu desconto é de 20%")
    print("O valor total é: "+str(preco))
    print("O valor com desconto é: "+str(resultado))
elif(preco >= 200 <=299):
    resultado = (10*preco)/100
    print("O seu desconto é de 10%")
    print("O valor total é: "+str(preco))
    print("O valor com desconto é: "+str(resultado))
elif(preco < 199):
    resultado = (5*preco)/100
    print("O seu desconto é de 5%")
    print("O valor total é: "+str(preco))
    print("O valor com desconto é: "+str(resultado))
else:
    print("Valor inválido!")