from dict import dict

def get_key(val):
    for key, value in dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"

choice = input('Digite 0 para codificar e 1 para decodificar: ')
k = int(input('Digite a chave: '))
textoplano = input('Digite a mensagem: ') #lista de char   tam = n
n = len(textoplano)
textocifrado = []#lista de char     ''
codigoplano = []#lista de inteiro   ''
cifradocodigo = []#lista de inteiro ''
textodecodificado = []



def cod(textoplano):
    for char in textoplano:
        if char in dict.keys():
            codigoplano.append(dict[char])
    i = 0
    while i < n:
        cifradocodigo.append((codigoplano[(k * i) % n] - i) % 28)
        #cifradocodigo[i] = (codigoplano[(k * i) % n] - 1) % 28 nao funfa
        textocifrado.append(get_key((codigoplano[(k * i) % n] - i) % 28))
        i += 1
    return ''.join(textocifrado)

def decod(textoplano):
    for char in textoplano:
        if char in dict.keys():
            textocifrado.append(dict[char])
    i = 0
    codigoplano = [None]*n
    while i < n:
        # cifradocodigo.append(get_key(int(textocifrado[i])))
        # print(f"cifracodigo: {cifradocodigo}")
        codigoplano[(k*i)%n] = (textocifrado[i] + i) % 28 
        i += 1
    for int in codigoplano:
        textodecodificado.append(get_key(int))
    return ''.join(textodecodificado)

if choice == '0': # codificar   ''
    # print(f"codigoplano: {codigoplano}")
    # print(f"cifradocodigo: {cifradocodigo}")
    # print(f"textocifrado: {textocifrado}")
    print("Frase final: ",cod(textoplano))
    
elif choice == '1': #decodificar
    print("Frase final: ", decod(textoplano))
