#dss 
import random

def modinv(x, y):
    d = 1
    while (d*x)%y!=1:
        d+=1
    return d

p = int(input("enter p: "))
q = int(input("Enter q: "))
m = int(input("enter hashed msg: "))
x = random.randint(0, q)
h = int(input("Enter h: "))

g = int((h*(p-1)/q)%p)
y = (g**x)%p
print(f"Public key by Alice (p, q, g, y): {p}, {q}, {g}, {y}")
while True:
    k = random.randint(1, q-1)
    if modinv(k, q)!=1:
        break
kinv = modinv(k, q)
r = ((g**k)%p)%q
s = (kinv*(m + (x*r)))%q
print(f"Signature (r, s): {r}, {s}")

sinv = modinv(s, q)
w = sinv%q
u1 = (m*w)%q
u2 = (r*w)%q
v = (((g**u1)*(y**u2))%p)%q

if (v==r):
    print(f"Verified as v = r = {r}")
else:
    print(f"Not verified as v = {v} and r = {r}")        
       