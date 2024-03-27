import random

p = int(input('Enter a prime number (p) : '))
g = int(input('Enter a number (g) : '))


class A:
	def __init__(self,n):
		self.n = n 

	def publish(self):
		return (g**self.n)%p

	def compute_secret(self, gb):
		return (gb**self.n)%p


class B:
	def __init__(self):
		self.a = random.randint(1, p)
		self.b = random.randint(1, p)
		self.arr = [self.a,self.b]

	def publish(self, i):
		return (g**self.arr[i])%p

	def compute_secret(self, ga, i):
		return (ga**self.arr[i])%p


na=int(input("Private key of Alice: "))
nb=int(input("Private key of Bob: "))
alice = A(na)
bob = A(nb)
darth = B()

print('\nPrivate selected number')
print(f'Alice Private selected number(a) : {alice.n}')
print(f'Bob Private selected number (b) : {bob.n}')
print(f'Darth selected private number for Alice (c) : {darth.a}')
print(f'Darth selected private number for Bob (d) : {darth.b}')

print('\nGenerating public values')
ga = alice.publish()
gb = bob.publish()
gea = darth.publish(0)
geb = darth.publish(1)
print(f'Alice public published number(ga): {ga}')
print(f'Bob public published number(gb): {gb}')
print(f'Darth published value for Alice (gc): {gea}')
print(f'Darth published value for Bob (gd): {geb}')

print('\nComputing the secret key')
sa = alice.compute_secret(gea)
sb = bob.compute_secret(geb)
print(f'Alice computed secret key (Ka) : {sa}')
print(f'Bob computed secret key (Kb) : {sb}')
