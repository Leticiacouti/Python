'''
Exemplo: abacaxi
a - d
b - e
c - f
x - a
i - l
Resultado: dedfdal
'''

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

mensagem = input("Digite a mensagem que será criptografada: ")
chave = 3
cifrada = " "
n = len(alfabeto) #Tamanho da lista alfabeto

print("Programa Simples de Criptografia")
print("Tamanho do alfabeto = ",n)

for letra in mensagem:
    indice = alfabeto.index(letra) #0 = alfabeto.index(a)
    print("Posição da letra = ",indice)
    nova_letra = alfabeto[(indice + chave) % n] #c = (0 + 3) % 26
    print("Novo Indice = ",nova_letra)
    cifrada = cifrada + nova_letra

print("Mensagem Original: ",mensagem)
print("Mensagem Cifrada: ",cifrada)
