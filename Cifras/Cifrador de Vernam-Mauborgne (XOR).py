#Cifrador de Vernam-Mauborgne (XOR)

msg = str(input("Insira a mensagem que precisa ser criptografada: "))
chave_k = str(input("Insira uma palavra que vai ser a chave: "))

msg_len = len(msg) #tamanho da mensagem
k_len = len(chave_k) #tamanho da chave
x = 0 #contador da mensagem
y = 0 #contadoe da chave
crypt = str("") #palavra criptografada
decrypt = str("") #palavra decifrada
o = str("")#letra criptografada/decifrada

print("Valores em ASCII letras criptografadas:")
for x in range(msg_len): #for para o tamanho da mensagem

    if k_len <= y:
        y = 0

    int_msg = ord(msg[x])
    int_k = ord(chave_k[y])

    if chr(int_msg) == ' ':
        o = int_msg

    else:
        o = ord(msg[x])^ord(chave_k[y])
        y = y + 1
    x = x + 1
    print(o)
    crypt = crypt + chr(o)

print("\nAgora decifrando a mensagem\n")

x = 0 #resetando os contadores
y = 0

for x in range(msg_len): #for para o tamanho da mensagem

    if k_len <= y:
        y = 0

    int_msg = ord(crypt[x])
    int_k = ord(chave_k[y])

    if chr(int_msg) == ' ':
        o = chr(int_msg)

    else: 
        o = chr(int_msg ^ int_k)
        y = y + 1

    x = x + 1
    decrypt = decrypt + o

print("Mensagem decifrada: " + decrypt + "\n\n")