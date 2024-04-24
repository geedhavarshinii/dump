# #crt
# def modinv(x, y):
#     d = 1
#     while (d * x) % y != 1:
#         d += 1
#     return d

# num_input = input("Enter nums: ")
# num = [int(x) for x in num_input.split()]

# rem_input = input("Enter rems: ")
# rem = [int(x) for x in rem_input.split()]

# k = len(num)
# M = 1
# for i in num:
#     M *= i

# zi = [M // n for n in num]
# yi = [modinv(zi[i], num[i]) for i in range(k)]

# print("M:", M)
# print("zi:", zi)
# print("yi:", yi)

# res = sum(rem[i] * zi[i] * yi[i] for i in range(k)) % M

# print("Result:", res)


# #rsa
# import random

# def gcd(a, b):
#     if a==0:
#         return b
#     return gcd(b%a, a)

# def mod_inverse(e, phi_n):
#     d = 1
#     while ((e*d)%phi_n != 1):
#         d+=1
#     return d   

# def generate(p, q):
#     n = p*q
#     phi_n = (p-1)*(q-1)
#     print('phi_n: ', phi_n)
#     e = 2
#     while gcd(e, phi_n)!=1:
#         e = e+1
#     print('e: ', e)
#     d = mod_inverse(e, phi_n)
#     print('d: ', d)
#     return n, e, d

# def encrypt(m, e, n):
#     c = m**e%n 
#     print(f"Encrypted message is {c}")
#     return c

# def decrypt(c, d, n):
#     m = c**d%n 
#     print(f"Decrypted message is {m}")   
#     return m

# p = int(input("Enter p: "))
# q = int(input("Enter q: "))
# m = int(input("Enter M: "))
# n, e, d = generate(p, q)
# c = encrypt(m, e, n)
# decrypt(c, d, n)

# #dss
# import random

# def modinv(x, y):
#     d = 1
#     while (x*d)%y!=1:
#         d+=1
#     return d

# def gcd(a, b):
#     if (a==0):
#         return b
#     return gcd(b%a, a)

# def rand_key(p):
#     k = 2
#     while gcd(k, p-1)!=1:
#         k = random.randint(2, p-2)
#     return k

# p = int(input("P: "))
# q = int(input("q: "))
# h = int(input("h: "))
# m = int(input("h(M): "))
# x = int(input("x: "))

# g = (h*(p-1)//q)%p
# y = pow(g, x)%p

# print(f"public key (p, q, g, y): {p}, {q}, {g}, {y}")

# k = rand_key(q)
# r = ((pow(g, k)%p)%q)
# kinv = modinv(k, q)
# s = (kinv * (m+x*r))%q

# print(f"Digital signature is {r} , {s}")

# w = modinv(s, q)%q
# u1 = (m * w)%q
# u2 = (r * w)%q
# v = ((g**u1)*(y**u2)%p)%q

# if (v==r):
#     print("verified")
# else:
#     print("not verified")

# #hillcipher
# def text_to_numbers(text):
#     return [ord(char.upper()) - 65 for char in text if char.isalpha]

# def numbers_to_text(numbers):
#     return ''.join(chr(num % 26 + 65) for num in numbers)

# def key_to_matrix(key, size):
#     key_numbers = text_to_numbers(key)
#     matrix = []
#     index = 0
#     for _ in range(size):
#         row = []
#         for _ in range(size):
#             row.append(key_numbers[index%len(key_numbers)])
#             index+=1
#         matrix.append(row)
#     return matrix

# def matrix_multiply(pt_mat, key_mat):
#     result = []
#     for row in key_mat:
#         value = sum(row[i]*pt_mat[i] for i in range(len(row)))
#         result.append(value%26)
#     return result

# def encrypt(pt, key):
#     pt_mat = text_to_numbers(pt)
#     key_mat = key_to_matrix(key, len(pt_mat))
#     encrypted_nums = matrix_multiply(pt_mat, key_mat)
#     return numbers_to_text(encrypted_nums)

# plaintext = input("Enter the pt: ")
# key = input("Enter the key: ")
# encrypted_text = encrypt(plaintext, key)
# print(f"Encrypted text is {encrypted_text}")

# #elgamal cryptography
# import random

# def modinv(x, y):
#     d = 1
#     while (d*x)%y!=1:
#         d+=1
#     return d

# q = int(input("Enter q: "))
# a = int(input("Enter a such that it is a primitive root of q: "))

# #key generation by alice
# xa = random.randint(0, q-1)
# ya = (a**xa)%q
# print(f"public key (q, a, ya) is {q}, {a}, {ya}")

# #encryption by bob with alice's public key
# m = int(input("Enter pt M: "))
# k = random.randint(0, q)
# K = (ya**k)%q
# c1 = (a**k)%q
# c2 = (K*m)%q
# print(f"Cipher text is {c1}, {c2}")

# #decryption by alice with alice's private key
# Ka = (c1**xa)%q
# Kinv = modinv(K, q)
# M = (c2*Kinv)%q
# print(f"Decrypted text is M : {M}")

# if (M==m):
#     print("Success")
# else:
#     print("failed")


# #elgamal ds
# import random

# def gcd(a, b):
#     if a==0:
#         return b
#     return gcd(b%a, a)

# def rand_key(p):
#     k = 2
#     while (gcd(k, p-1)!=1):
#         k = random.randint(2, p-2)
#     return k

# def modinv(x, y):
#     d = 1
#     while ((d*x)%y!=1):
#         d+=1
#     return d

# p = int(input("Enter p: "))
# g = int(input("Enter g: "))
# d = random.randint(2, p-2)
# e = (g**d)%p
# print(f"Public key (p, g, e): {p}, {g}, {e}")
# print(f"Private key(d): {d}")

# m = int(input("Enter the hashed message : "))
# k = rand_key(p)
# y1 = (g**k)%p
# kinv = modinv(k, p-1)
# y2 = (kinv*(m-(d*y1)))%(p-1)
# print(f"Elgamal based DS (y1, y2): {y1}, {y2}")
# print(f"\nVerification:")
# v1 = (g**m)%p
# v2 = ((e**y1)*(y1**y2))%p
# if (v1==v2):
#     print(f"Verified as v1 = v2 = {v1}")
# else:
#     print(f"not verified as v1 = {v1} and v2 = {v2}")

# #sdes key generation
# def apply_table(inp, table):
#     res = ""
#     for i in table:
#         res += inp[i-1]
#     return res

# def left_shift(data):
#     return data[1:]+data[0]

# if __name__ == "__main__":
#     key = input("Enter 10 bit key: ")
#     message = input("Enter 8 bit message: ")
#     p8 = [6, 3, 7, 4, 8, 5, 10, 9]
#     p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
#     #key generation
#     temp = apply_table(key, p10)
#     left = temp[:5]
#     right = temp[5:]
#     left = left_shift(left)
#     right = left_shift(right)
#     key1 = apply_table(left+right, p8)
#     print("Key 1 is ", key1)
#     left = left_shift(left)
#     right = left_shift(right)
#     left = left_shift(left)
#     right = left_shift(right)
#     key2 = apply_table(left+right, p8)
#     print("Key 2 is ", key2)

# #ecc cryptography
# def modinv(x, y):
#     d = 1
#     while (d*x)%y!=1:
#         d+=1
#     return d

# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# a = int(input("a: "))
# b = int(input("b: "))
# p = int(input("p: "))

# if x1==x2 and y1==y2:
#     mod_inv = modinv(2*y1, p)
#     lamda = ((3*x1*x1+a)*mod_inv)%p
#     x3 = (lamda**2-x1-x2)%p
#     y3 = (lamda*(x1-x3)-y1)%p
#     print(f"the sum is {x3}, {y3}")

# else:
#     mod_inv = modinv(x1-x2, p)
#     lamda = ((y1-y2)*mod_inv)%p
#     x3 = (lamda**2-x1-x2)%p
#     y3 = (lamda*(x1-x3)-y1)%p
#     print(f"The sum is {x3}, {y3}")

# #mitm algorithm
# import random
# p = int(input("Enter a prime number p: "))
# g = int(input("Enter a number g: "))
# class A:
#     def __init__(self, n):
#         self.n = n
#     def publish(self):
#         return (g**self.n)%p
#     def compute_secret(self, gb):
#         return (gb**self.n)%p

# class B: 
#     def __init__(self):
#         self.a = random.randint(1, p)
#         self.b = random.randint(1, p)
#         self.arr = [self.a, self.b]
#     def publish(self, i):
#         return (g**self.arr[i])%p
#     def compute_secret(self, ga, i):
#         return (ga**self.arr[i])%p
    
# na = int(input("Private key of Alice: "))
# nb = int(input("Private key of Bob: "))
# alice = A(na)
# bob = A(nb)
# darth = B()

# print("\nPrivate selected numbers:")
# print(f"Alice selected number(a): {alice.n}")
# print(f"Bob selected number (b): {bob.n}")
# print(f"Darth selected number for Alice (C): {darth.a}")
# print(f"Darth selected number for Bob (d): {darth.b}")

# print("\nGenerating public values: ")
# ga = alice.publish()
# gb = bob.publish()
# gda = darth.publish(0)
# gdb = darth.publish(1)
# print(f"Alice's public number (ga): {ga}")
# print(f"Bob's public number (gb): {gb}")
# print(f"Darth's public number for Alice (gda): {gda}")
# print(f"Darth's public number for Bob (gdb): {gdb}")

# print("the secret key is: ")
# sa = alice.compute_secret(gda)
# sb = bob.compute_secret(gdb)
# print(f"Alice computed the secret key as (Ka): {sa}")
# print(f"Bob computed secret key as (Kb): {sb}")

# #dh
# p = int(input("Enter p: "))
# g = int(input("Enter g: "))
# a = int(input("Enter secret key of Alice: "))
# b = int(input("Enter secret key of Bob: "))
# y1, y2 = pow(g, a)%p, pow(g, b)%p
# k1, k2 = pow(y2, a)%p, pow(y1, b)%p
# print(f"The keys are: {k1}, {k2}")

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