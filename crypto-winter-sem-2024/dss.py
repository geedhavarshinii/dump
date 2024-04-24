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
    while gcd(k, p-1)!=1:
        k = random.randint(2, p-2)
    return k

p = int(input("P: "))
q = int(input("q: "))
h = int(input("h: "))
m = int(input("h(M): "))
x = int(input("x: "))

g = (h*(p-1)//q)%p
y = pow(g, x)%p

print(f"public key (p, q, g, y): {p}, {q}, {g}, {y}")

k = rand_key(q)
r = ((pow(g, k)%p)%q)
kinv = modinv(k, q)
s = (kinv * (m+x*r))%q

print(f"Digital signature is {r} , {s}")

w = modinv(s, q)%q
u1 = (m * w)%q
u2 = (r * w)%q
v = ((g**u1)*(y**u2)%p)%q

if (v==r):
    print("verified")
else:
    print("not verified")


# #dss 
# import random

# def modinv(x, y):
#     d = 1
#     while (d*x)%y!=1:
#         d+=1
#     return d

# p = int(input("enter p: "))
# q = int(input("Enter q: "))
# m = int(input("enter hashed msg: "))
# x = random.randint(0, q)
# h = int(input("Enter h: "))

# g = int((h*(p-1)/q)%p)
# y = (g**x)%p
# print(f"Public key by Alice (p, q, g, y): {p}, {q}, {g}, {y}")
# while True:
#     k = random.randint(1, q-1)
#     if modinv(k, q)!=1:
#         break
# kinv = modinv(k, q)
# r = ((g**k)%p)%q
# s = (kinv*(m + (x*r)))%q
# print(f"Signature (r, s): {r}, {s}")

# sinv = modinv(s, q)
# w = sinv%q
# u1 = (m*w)%q
# u2 = (r*w)%q
# v = (((g**u1)*(y**u2))%p)%q

# if (v==r):
#     print(f"Verified as v = r = {r}")
# else:
#     print(f"Not verified as v = {v} and r = {r}")        
       