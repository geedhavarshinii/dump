def encryptdecrypt(word, key):
    enres, deres='', ''
    for i in range(len(word)):
        ch = word[i]
        if ch==" ":
            enres+=" "
        elif (ch.isupper()):
            enres+=chr(ord('A')+(ord(word[i])-ord('A')+key)%26);
        else:
            enres+=chr(ord('a')+(ord(word[i])-ord('a')+key)%26);
    for i in range(len(enres)):
        char = enres[i]
        if char==" ":
            deres += " "
        elif (ch.isupper()):
            deres+=chr(ord('A')+(ord(enres[i])-ord('A')-key)%26)
        else:
            deres+=chr(ord('a')+(ord(enres[i])-ord('a')-key)%26)
    return enres, deres

word = input("Enter the word to be encrypted and decrypted: ")
key = int(input("Enter the key to be used to shift: "))
encrypted, decrypted = encryptdecrypt(word, key)
print(encrypted, decrypted)