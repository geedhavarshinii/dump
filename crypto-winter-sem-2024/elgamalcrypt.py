def mod(x,y):
    d=1
    while (x*d)%y!=1:
        d+=1
    return d

x1= int(input("x1: "))
y1= int(input("y1: "))
x2= int(input("x2: "))
y2= int(input("y2: "))
a=int(input("a: "))
b=int(input("b: "))
p=int(input("p: "))

if x1==x2 and y1==y2:
    modinv=mod(2*y1,p)
    lamda=((3*x1*x1+a)*modinv)%p
    x3=(lamda**2-x1-x2)%p
    y3=(lamda*(x1-x3)-y1)%p
    print("The sum is: ")
    print(x3,y3)
else:
    modinv=mod(x1-x2,p)
    lamda=((y1-y2)*modinv)%p
    x3=(lamda**2-x1-x2)%p
    y3=(lamda*(x1-x3)-y1)%p
    print("The sum is: ")
    print(x3,y3)