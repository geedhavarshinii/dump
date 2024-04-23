def modinv(x, y):
    d = 1
    while (d * x) % y != 1:
        d += 1
    return d

num_input = input("Enter nums: ")
num = [int(x) for x in num_input.split()]

rem_input = input("Enter rems: ")
rem = [int(x) for x in rem_input.split()]

k = len(num)
M = 1
for i in num:
    M *= i

zi = [M // n for n in num]
yi = [modinv(zi[i], num[i]) for i in range(k)]

print("M:", M)
print("zi:", zi)
print("yi:", yi)

res = sum(rem[i] * zi[i] * yi[i] for i in range(k)) % M

print("Result:", res)


# def inv(a, m) : 
# 	m0 = m 
# 	x0 = 0
# 	x1 = 1
# 	if (m == 1) : 
# 		return 0
# 	while (a > 1) : 
# 		q = a // m 
# 		t = m 
# 		m = a % m 
# 		a = t 
# 		t = x0 
# 		x0 = x1 - q * x0 
# 		x1 = t 
# 	if (x1 < 0) : 
# 		x1 = x1 + m0 
		
# 	return x1 

# def findMinX(num, rem, k) : 
# 	prod = 1
# 	for i in range(0, k) : 
# 		prod = prod * num[i] 
# 	result = 0
# 	for i in range(0,k): 
# 		pp = prod // num[i] 
# 		result = result + rem[i] * inv(pp, num[i]) * pp 
		
# 	return result % prod 

# num_input = input("Enter numbers separated by spaces: ")
# num = [int(x) for x in num_input.split()]

# rem_input = input("Enter remainders separated by spaces: ")
# rem = [int(x) for x in rem_input.split()]

# k = len(num) 
# print("x is", findMinX(num, rem, k)) 