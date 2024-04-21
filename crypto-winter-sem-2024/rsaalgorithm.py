import random

def gcd(a, b):
    if a==0:
        return b
    return gcd(b%a, a)

def mod_inverse(e, phi_n):
    d = 1
    while ((e*d)%phi_n != 1):
        d+=1
    return d   

def generate(p, q):
    n = p*q
    phi_n = (p-1)*(q-1)
    print('phi_n: ', phi_n)
    e = 2
    while gcd(e, phi_n)!=1:
        e = e+1
    print('e: ', e)
    d = mod_inverse(e, phi_n)
    print('d: ', d)
    return n, e, d

def encrypt(m, e, n):
    c = m**e%n 
    print(f"Encrypted message is {c}")
    return c

def decrypt(c, d, n):
    m = c**d%n 
    print(f"Decrypted message is {m}")   
    return m

p = int(input("Enter p: "))
q = int(input("Enter q: "))
m = int(input("Enter M: "))
n, e, d = generate(p, q)
c = encrypt(m, e, n)
decrypt(c, d, n)



# import random
# from sympy import mod_inverse, totient, gcd

# def generate(p,q):
#         n = p * q
#         phi_n = totient(n)
#         print('phi(n)=',phi_n)
#         e = 2
#         while gcd(e, phi_n) != 1:
#                 e = e+1
#         print('e=',e)
#         d = mod_inverse(e, phi_n)
#         print('d=',d)
#         return n,e,d

# def encrypt(M,e,n):
#         c=M**e%n
#         print("Encrypted (c)=",c)
#         return c

# def decrypt(c,d,n):
#         M=c**d%n
#         print("Decrypted (M)=",M)
#         return M

# p=int(input("Enter P: "))
# q=int(input("Enter Q: "))

# M=int(input("Enter M: "))

# n,e,d=generate(p,q)

# c=encrypt(M,e,n)
# decrypt(c,d,n)








