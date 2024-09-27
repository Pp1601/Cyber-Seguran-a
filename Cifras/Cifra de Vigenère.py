"""
Cifra de Vigenère

O código a seguir diz respeiito a parte da Criptografia

"""

#Coletando informções quanto mensagem e chave
msg = input("\nEscreva a mensagem que precisa de criptografia: ")
key = input("Escreva a chave para a criptografia: ")

#matriz principal da criptografia
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
matriz = [alfabeto[i:] + alfabeto[:i] for i in range(len(alfabeto))]

msg_len = len(msg)
key_len = len(key)
print(matriz)
#Função que iguala o tamanho da chave ao tamanho da msg
def key_aligner(original_key):

    x = 0 #contadores
    y = 0
    aligned_key = str("")

    for x in range(msg_len):

        if msg[x] == ' ':
            aligned_key = aligned_key + ' '

        else:
            aligned_key = aligned_key + original_key[y]
            y = y + 1

        if y >= key_len:
            y=0
            

    return aligned_key

#Função que criptografa a mensagem
def crypt_msg(msg, key):
    
    crypt_txt = str('')
    x = 0

    for x in range(msg_len):

        line_key = None
        column_msg = None
        y = 0

        if msg[x] == ' ':
            crypt_txt = crypt_txt + ' '

        else:
            while line_key == None:
                if key[x] == alfabeto[y]:
                    line_key = y
                else:
                    y = y + 1

            y = 0

            while column_msg == None:
                if msg[x] == alfabeto[y]:
                    column_msg = y
                else:
                    y = y + 1

            crypt_txt = crypt_txt + matriz[line_key][column_msg]

    return crypt_txt

key = key_aligner(key)

crypt = crypt_msg(msg, key)

print("\nMsg: " + msg + "||Aligned key: " + key)
print("\nPalavra criptografada: " + crypt)

"""
O código a seguir diz respeito a parte da Decifragem.

Atenção ele utiliza alguns elementos do código anterior como a chave e algumas outras variaveis

"""
#Função que decifra a mensagem
def decrypt_msg(crypt, key):

    decrypt = str("")
    x = 0

    for x in range(msg_len):

        line_key = None
        column_crypt = None
        y = 0

        if crypt[x] == ' ':
            decrypt = decrypt + ' '
        
        else:
            while line_key == None:
                if key[x] == alfabeto[y]:
                    line_key = y
                else:
                    y = y + 1

            y = 0

            while column_crypt == None:
                if crypt[x] == matriz[line_key][y]:
                    column_crypt = y
                else:
                    y = y + 1

            decrypt = decrypt + matriz[0][y]

    return decrypt
    
print("\nPalavra decifrada: "+ decrypt_msg(crypt, key))