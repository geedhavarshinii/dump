import random

def modinv(x, y):
    d = 1
    while (d*x)%y!=1:
        d+=1
    return d

q = int(input("Enter q: "))
a = int(input("Enter a such that it is a primitive root of q: "))

#key generation by alice
xa = random.randint(0, q-1)
ya = (a**xa)%q
print(f"public key (q, a, ya) is {q}, {a}, {ya}")

#encryption by bob with alice's public key
m = int(input("Enter pt M: "))
k = random.randint(0, q)
K = (ya**k)%q
c1 = (a**k)%q
c2 = (K*m)%q
print(f"Cipher text is {c1}, {c2}")

#decryption by alice with alice's private key
Ka = (c1**xa)%q
Kinv = modinv(K, q)
M = (c2*Kinv)%q
print(f"Decrypted text is M : {M}")

if (M==m):
    print("Success")
else:
    print("failed")
