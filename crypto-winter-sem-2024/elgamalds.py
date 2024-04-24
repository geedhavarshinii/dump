import random

def modinv(x, y):
    d = 1
    while (x*d)%y!=1:
        d+=1
    return d
def gcd(a, b):
    if (a==0): 
        return b
    return gcd(b%a, a)
def rand_key(p):
    k = 2
    while (gcd(k, p-1)!=1):
        k = random.randint(2, p-2)
    return k

p = int(input("P: "))
g = int(input("g: "))
d = random.randint(2, p-2)
e = (g**d)%p

print(f'\nPublic Key [p,g,e]: [{p},{g},{e}]')
print(f'Private key: {d}\n')

m = int(input("H(M): "))
k = rand_key(p)
y1 = (g**k)%p
kinv = modinv(k, p-1)
y2 = (kinv*(m-(d*y1)))%(p-1)
print(f"\nElgamal based Digital Signature (y1, y2): ({y1}, {y2})")
print("\nVerification: ")
v1 = (g**m)%p
v2 = ((e**y1)*(y1**y2))%p
if (v1==v2):
    print(f"\nVerified as v1 = v2 = {v1}\n")
else:
    print(f"\nNot verified as v1 = {v1} and v2 = {v2}")
