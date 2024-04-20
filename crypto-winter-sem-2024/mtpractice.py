# #playfair cipher
# def playfair_cipher(pt, key, mode):
#     alphabet = 'abcdefghiklmnopqrstuvwxyz'
#     key = key.lower().replace(' ', '').replace('j', 'i')

#     key_square = ''
#     for letter in key + alphabet:
#         if letter not in key_square:
#             key_square += letter

#     pt = pt.lower().replace(' ', '').replace('j', 'i')
#     if (len(pt)%2 == 1):
#         pt += 'x'
#     digraphs = [pt[i:i+2] for i in range(0, len(pt), 2)]

#     def encrypt(digraph):
#         a, b = digraph
#         row_a, col_a = divmod(key_square.index(a), 5)
#         row_b, col_b = divmod(key_square.index(b), 5)
#         if (row_a == row_b):
#             col_a = (col_a + 1)%5
#             col_b = (col_b + 1)%5
#         elif (col_a == col_b):
#             row_a = (row_a + 1)%5
#             row_b = (row_b + 1)%5
#         else:
#             col_a, col_b = col_b, col_a
#         return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]
    
#     def decrypt(digraph):
#         a, b = digraph
#         row_a, col_a = divmod(key_square.index(a), 5)
#         row_b, col_b = divmod(key_square.index(b), 5)
#         if row_a == row_b:
#             col_a = (col_a - 1)%5
#             col_b = (col_b - 1)%5
#         elif col_a == col_b:
#             row_a = (row_a - 1)%5
#             row_b = (row_b - 1)%5
#         else:
#             col_a, col_b = col_b, col_a
#         return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]
    
#     result = ''
#     for digraph in digraphs:
#         if mode == 'encrypt':
#             result += encrypt(digraph)
#         elif mode == 'decrypt':
#             result += decrypt(digraph)
#     return result

# pt = input("Enter the text to be encrypted: ")
# key = input("\nEnter the key: ")
# ciphertext = playfair_cipher(pt, key, 'encrypt')
# print(f"\nthe encrypted text is {ciphertext}.")
# detext = playfair_cipher(ciphertext, key, 'decrypt')
# print(f"\nThe decrypted text is {detext}.\n")

# #extended euclidean 
# def gcdExtended(a, b):
#     if a==0:
#         return b, 0, 1
#     gcd, x1, y1 = gcdExtended(b%a, a)
#     x = y1 - (b//a) * x1
#     y = x1

#     return gcd, x, y

# a, b = int(input("Enter a: ")), int(input("Enter b: "))
# gcd, x, y = gcdExtended(a, b)
# print(f"gcd of {a} and {b}: {gcd}\nx: {x}\ny: {y}")

# #monoalphabetic cipher
# import random

# def generate_cipher_key():
#     alphabet = 'abcdefghijklmnopqrstuvwxuyz'
#     shift = random.randint(1, 26)
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     key = dict(zip(alphabet, shifted_alphabet))
#     return key
# def encrypt(message, key):
#     encrypted_msg = ''
#     for char in message: 
#         if char.isalpha():
#             if char.islower():
#                 encrypted_msg += key[char]
#             else:
#                 encrypted_msg += key[char.lower()].upper()
#         else:
#             encrypted_msg += char
#     return encrypted_msg
# def decrypt(ciphertext, key):
#     reverse_key = {v:k for k, v in key.items()}
#     decrypted_msg = ''
#     for char in ciphertext:
#         if char.isalpha():
#             if char.islower():
#                 decrypted_msg += reverse_key[char]
#             else:
#                 decrypted_msg += reverse_key[char.islower()].upper()
#         else:
#             decrypted_msg += char
#     return decrypted_msg

# def main():
#     key = generate_cipher_key()
#     plaintext = input("Enter message to be encrypted: ")
#     encrypted = encrypt(plaintext, key)
#     print(f"\nEncrypted message: {encrypted}")
#     print(f"\nDecrypted message: {decrypt(encrypted, key)}")

# if __name__ == "__main__":
#     main()



# #caesar cipher
# def encryptdecrypt(word, key):
#     enres, deres = '', ''
#     for i in range(len(word)):
#         ch = word[i]
#         if ch==" ":
#             enres+=" "
#         elif (ch.isupper()):
#             enres += chr(ord('A') + (ord(word[i]) - ord('A') + key) % 26)
#         else:
#             enres += chr(ord('a') + (ord(word[i]) - ord('a') + key) % 26)
#     for i in range(len(enres)):
#         char = enres[i]
#         if char==" ":
#             deres += " "
#         elif (char.isupper()):
#             deres += chr(ord('A') + (ord(char[i]) - ord('A') - key) % 26)
#         else:
#             deres += chr(ord('a') + (ord(enres[i]) - ord('a') - key) % 26)
#     return enres, deres

# word = input("Enter the word to be encrypted and decrypted using Caesar Cipher: ")
# key = int(input("\nEnter the key to be used for shifting: "))
# encrypted, decrypted = encryptdecrypt(word, key)
# print(f"\nThe encrypted version of the given word is {encrypted}. The decrypted version is {decrypted}.\n")