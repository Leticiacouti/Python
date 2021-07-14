alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

n = len(alfabeto)

modo = input("Escolha (E) para encriptar ou (D) para decriptar o texto: ")
mensagem = input("Digite a mensagem a ser encriptada ou decifrada: ")
chave = int(input("Entre com o valor da chave (deslocamento): "))

def funcao_cripto(msg, key):
    cifrada = ""
    for letra in msg:
        indice = alfabeto.index(letra)
        nova_letra = alfabeto[(indice + key) % n]
        cifrada = cifrada + nova_letra
    return cifrada

def funcao_descripto(msg, key):
    cifrada = ""
    for letra in msg:
        indice = alfabeto.index(letra)
        nova_letra = alfabeto[(indice - key) % n]
        cifrada = cifrada + nova_letra
    return cifrada

if(modo == 'E'):
    print("Original: ",mensagem)
    print("Mensagem Criptografada: ", funcao_cripto(mensagem,chave))
elif(modo == 'D'):
    print("Original: ",mensagem)
    print("Mensagem Descriptografada: ", funcao_descripto(mensagem,chave))