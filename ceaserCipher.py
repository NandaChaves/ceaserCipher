import math
#1º gerar o array do alfabeto
alfa =[' ','a', 'b', 'c', 'd', 'e','f','g','h','i ','j','k','l','m','n','o', 'p', 'q', 'r', 's', 't', 'u','v','w','x','y','z']
#criar o texto e a chave
texto="russia vs ucrania"
chave='d'
#descobrir a posição da chave no alfabeto
for i in range(len(alfa)):
    if alfa[i] == chave:
        print("%s está na posicao %s"%(chave,i))
        indice = i
print("Posição da chave= ", indice)
encrip= ""
for j in range(len(texto)):
    soma=0
    #descobrir valor do caracter no alfabeto
    for x in range(len(alfa)):
        if texto[j] == alfa[x]:
            soma = x + indice
            if soma >= len(alfa):
                soma = soma - len(alfa)
    encrip += alfa[soma]
print('Texto encriptado:' + encrip)

def desencri(encrip):
    for i in range(len(alfa)):
        chave = 'd'
        if alfa[i] == chave:
            print("%s está na posicao %s" % (chave, i))
            ind = i
    print("Posição da chave= ", ind)
    desencrip = ""
    for j in range(len(texto)):
        soma = 0
        # descobrir valor do caracter no alfabeto
        for x in range(len(alfa)):
            if texto[j] == alfa[x]:
                soma = x - (ind-4)
                if soma < 0:
                    soma = soma + len(alfa)
        desencrip = desencrip + alfa[soma]
    return 'Texto desencriptado:' + desencrip

print(desencri(encrip))



