'''
Considere o arquivo notas_estudantes.dat que contém uma linha para cada aluno de uma turma de estudantes. 
O nome de cada estudante está no início de cada linha e é seguido pelas suas notas. 
 
Aluno 	P1 	TP1 	NP1 	P2  	TP2 	NP2 	MG 	EX 	MGF 
Jose 	3.5 0.0 	 	    5.5 	1.5 	 	 	 	 
Pedro 	7.5 2.0 	 	    7.5 	1.0 	 	 	 	 
Suzana 	6.5 1.5 	 	    5.5 	1.5 	 	 	 	 
Gisela 	8.0 2.0 	 	    7.5 	1.0 	 	 	 	 
João 	3.5 0.0 	 	    5.5 	0.0 	 	 	 	 
Andre 	6.0 1.5 	 	    7.0 	1.0 	 	 	 	 
Carlos 	1.5 0.0 	 	    4.0 	0.0 	 	 	 	 
Natalia 6.0 2.0 	 	    5.5 	1.5 	 	 	 	 
Tabela A: notas_estudantes.dat  					
 
Fórmulas (Regras de Negócio)  
1)	NP1 = P1 (0-8) + TP1 (0-2) 
2)	NP2 = P2 (0-8) + TP2 (0-2) 
3)	MG = (NP1 + NP2)/2   Aprova direto com 7.0 =>MG =< 10.0 
4)	Caso o aluno tenha uma média (MG =<7) ele terá direito a realizar o exame.
Onde a média de aprovação deve ser maior ou igual a 5.0 (MGF => 5.0) 
5)	Caso contrário o aluno ficará em dependência (DP)
'''

#Exercicio 2
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("-" * 65)

with open('d:/Letícia/Faculdade/Segundo Semestre/Introdução à Programação Estruturada/Python/tp6/notas_estudantes.dat',
'w', encoding='utf-8') as arq:

    alunos = 'José,3.5,0.0,5.5,1.5\nPedro,7.5,2.0,7.5,1.0\nSuzana,6.5,1.5,5.5,1.5\nGisela,8.0,2.0,7.5,1.0\nJoão,3.5,0.0,5.5,0.0\nAndre,6.0,1.5,7.0,1.0\nCarlos,1.5,0.0,4.0,0.0\nNatalia,6.0,2.0,5.5,1.5'
    arq.write(alunos)

with open('d:/Letícia/Faculdade/Segundo Semestre/Introdução à Programação Estruturada/Python/tp6/notas_estudantes.dat',
'r', encoding='utf-8') as arq:
    texto = arq.read()
    linhas = texto.split('\n')

    for i, linha in enumerate(linhas):
        linhas[i] = linha.split(',')

    for i, linha in enumerate(linhas):
        linhas[i].append((float(linha[1]) + float(linha[2]) + float(linha[3]) + float(linha[4])) / 2)
        print('Aluno: '+linha[0]+" sua média geral é: ",linha[5])
        print("-" * 65)
    
    for i, linha in enumerate(linhas):
        if linha[5] >= 7:
            print('Aluno: '+linha[0]+" foi aprovado!")
            print("-" * 65)
    
    max_coluna = 0

    for i in range(0,len(linhas)-1,1):
        max_coluna = linhas[i][5] if linhas[i][5] > max_coluna else max_coluna

    min_coluna = max_coluna

    for i in range(0,len(linhas)-1,1):
        min_coluna = linhas[i][5] if linhas[i][5] < min_coluna else min_coluna

    print('O minimo da turma é: ',min_coluna)
    print("-" * 65)
    print('O maximo da turma é: ',max_coluna)
    print("-" * 65)

    for i, linha in enumerate(linhas):
        nota_minima = 0
        nota_maxima = 0
        p1 = float(linha[1]) + float(linha[2])
        p2 = float(linha[3]) + float(linha[4])

        if p1 > p2:
            nota_maxima = p1
            nota_minima = p2
        elif p2 > p1:
            nota_maxima = p2
            nota_minima = p1

        print('Aluno: '+linha[0]+' sua nota minima é: ',nota_minima,'e sua nota maxima é: ',nota_maxima)
        print("-" * 65)

    for i, linha in enumerate(linhas):
        if linha[5] < 7:
            print('Aluno: '+linha[0]+' pegou exame!')
            print("-" * 65)        