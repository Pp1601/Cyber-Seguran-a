"""

Nome: Pedro Paulo Gadioli
Ra: 22009447

Questão 1

"""
#Decifra César

#Coletando dados
print("Cifra de Cesar\n")
msg = str(input("Insira a mensagem que precisa de criptografia: "))
k = 5 #Chave encontrada

#Identificando o tamanho da string e adicionando alguns parametros
msg = msg.lower()
i = len(msg) #Tamanho da string
x = 0  #Contador
decrypt = str("") #Frase criptografada
o = str("") #Letra criptografada/decifrada
parametro = int
dif = int

decrypt = str("") #Frase criptografada
for x in range(i):
        
        ascii_char = ord(msg[x]) #Transformando caractéres em decimais

        if chr(ascii_char) == 'a':
            parametro = 0
        elif (ascii_char - k) == 96:
            parametro = 1
        elif (ascii_char - k) < 96 and chr(ascii_char) != ' ' and chr(ascii_char) != 'a':
            parametro = 2
        else:
            parametro = 3

        if(parametro == 0):
            ascii_char = 122 - (k - 1)
            o = chr(ascii_char)

        elif(parametro == 1):
            ascii_char = 122
            o = chr(ascii_char)

        elif(parametro == 2):
            dif = (ascii_char - k) - 97
            ascii_char = 122 - (k + dif)
            o = chr(ascii_char)

        elif(parametro == 3):
            if chr(ascii_char) == ' ': #Desconsidreando os espaços
                o = chr(ascii_char)
            else:
                o = chr(ascii_char - k) #Retornando as letras conforme o valor da chave

        decrypt = decrypt + o #Concatenação da letra decifrada com a palavra decifrada
        x = x + 1
print(k)
print("Palavra decifrada: " + decrypt)
