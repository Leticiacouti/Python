'''
Usando apenas os modos de abertura de arquivos mostrados nesta aula (‘w’ e ‘r’) faça o seguinte: 
1.	Inverta a ordem da lista e grave em um segundo arquivo. 
2.	Ordene a lista alfabeticamente em um terceiro arquivo. 
3.	Com a lista organizada faça a sua numeração em um quarto arquivo, assim: 
•	1 - Clio 
•	2 - EcoSport…
'''

#Exercicio 1
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")
    
with open('d:/Letícia/Faculdade/Segundo Semestre/Introdução à Programação Estruturada/Python/tp6/lista.txt',
'w+', encoding = 'utf-8') as arq:
    arq.write('''•	Golf
•	Strada
•	Clio
•	EcoSport
•	Palio
•	Uno
•	Gol''')

print("A lista invertida foi salva com sucesso!")