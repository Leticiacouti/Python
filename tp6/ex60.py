'''
Exercício Fix61  
Usando apenas os modos de abertura de arquivos mostrados nesta aula (‘w’ e ‘r’) faça o seguinte: Grave esta lista em um arquivo (Copie para o seu código para isso): 
•	Gol 
•	Uno 
•	Palio 
•	EcoSport 
•	Clio 
•	Strada 
•	Golf 
'''

#Exercicio 0
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

contador = 0

arq = open('d:/Letícia/Faculdade/Segundo Semestre/Introdução à Programação Estruturada/Python/tp6/lista.txt',
'r', encoding = "utf-8")

for linha in arq:
    linha = linha.rstrip()
    contador = contador + 1
    print(linha)
print("")
print("Foram encontradas {} linhas.".format(contador))

arq.close()