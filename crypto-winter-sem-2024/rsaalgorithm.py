import random
from sympy import mod_inverse, totient, gcd

def generate(p,q):
        n = p * q
        phi_n = totient(n)
        print('phi(n)=',phi_n)
        e = 2
        while gcd(e, phi_n) != 1:
                e = e+1
        print('e=',e)
        d = mod_inverse(e, phi_n)
        print('d=',d)
        return n,e,d

def encrypt(M,e,n):
        c=M**e%n
        print("Encrypted (c)=",c)
        return c

def decrypt(c,d,n):
        M=c**d%n
        print("Decrypted (M)=",M)
        return M

p=int(input("Enter P: "))
q=int(input("Enter Q: "))

M=int(input("Enter M: "))

n,e,d=generate(p,q)

c=encrypt(M,e,n)
decrypt(c,d,n)








