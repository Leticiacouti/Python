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

mensagem = "DeDFd[L#Jrvwrvr"
mensagem = mensagem.lower()
chave = 3
cifrada = " "
#n = len(alfabeto) #Tamanho da lista alfabeto
n = 128 #Tamanho da tabela ASCII

def funcao_descripto(msg, key):
    cifrada = ""
    for letra in msg:
        indice = ord(letra)
        nova_letra = chr((indice + key) % n)
        cifrada = cifrada + nova_letra
    return cifrada

print("Original: ",mensagem)
print("Mensagem Descriptografada: ", funcao_descripto(mensagem,chave))