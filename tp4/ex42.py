'''
Exercício Fix42 
Elaborar um algoritmo (programa) que leia as notas de 5 alunos e retorne a maior nota da turma.
Utilize a estrutura de controle while.   
'''

#Exercicio 2
print("Letícia Coutinho da Silva - N5752E4 - CC2A41")
print("--------------------------------------------")

nota = 0
MaiorNota = 0
i = 0

while(i < 5):
    nota = (float(input("Digite a nota do {}º aluno: ".format(i+1))))
    if (1 == 0):
        MaiorNota = nota

    else:
        if(nota > MaiorNota):
            MaiorNota = nota
    
    i +=1

print("A maior nota digitada foi {}".format(MaiorNota))
