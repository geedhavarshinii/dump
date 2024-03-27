P = int(input("Enter P:"))
G = int(input("Enter G: "))
a = int(input("Secret key of Alice:"))
b = int(input("Secret key of Bob: "))
y1, y2 = pow(G, a) % P, pow(G, b) % P
k1, k2 = pow(y2, a) % P, pow(y1, b) % P
print(k1, k2)