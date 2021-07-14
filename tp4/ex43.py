'''
Exercício Fix43 
Elaborar um algoritmo (programa) que determine se a pessoa está com no seu Peso Ideal (ou não) e IMC.  
Onde o usuário deverá digitar o peso, o sexo e a altura de uma determinada pessoa. Após a execução,
deverá exibir se esta pessoa está ou não com seu peso ideal. Veja tabela (a) e (b) da relação peso/altura². 

Incluir uma mensagem na qual deverá aparecer o seu nome, RA e turma antes do resultado final, depois faça um
(print screen) e comentar o(s) resultado(s) do programa após a execução do mesmo. 

Tabela a: IMC para mulheres 	Tabela b: IMC para homens
(Tabelas na Apostila)
'''

#Exercicio 3
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
print("Programa que determina se a pessoa está com seu Peso Ideal")
print("")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
sexo = input("Digite F se seu sexo for feminino ou M se for masculino: ").upper()
imc = peso / (altura * altura)
if(sexo == 'F'):
    if(imc < 19):
        print("Você está abaixo do peso!")
    elif(19 <= imc < 24):
        print("Você está no peso ideal!")
    elif(imc >= 24):
        print("Você está acima do peso!")
elif(sexo == 'M'):
    if(imc < 20):
        print("Você está abaixo do peso!")
    elif(20 <= imc < 25):
        print("Você está no peso ideal!")
    elif(imc <= 25):
        print("Você está acima do peso!")
else:
    print("Valor inválido!")