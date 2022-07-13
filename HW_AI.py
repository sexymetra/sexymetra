def sl(num):
    L = []
    if num <= 1000:
        for i in range(1000//num):
            L.append(num*(i+1))
        return L
    else:
        return L

def not_sl(num1,num2):
    L = [i+1 for i in range(1000)]
    for i in sl(num1):
        if i in L:
            L.remove(i)
    for j in sl(num2):
        if j in L:
            L.remove(j)
    return sum(L)

def prime(num):
    L = []
    for i in range(2, num):
        if num % i ==0:
            L.append(i)
    if not L:
        print(f"{num} is a prime number.")
    return L+[num]

def homework(a,b):
    import math
    a=int(a)
    b=int(b)
    L=[]
    for i in range(1,1001):
        if (math.gcd(a,i) == 1) & (math.gcd(b, i) == 1):
            L.append(i)
    
    return(sum(L))
a,b = map(int, input().split())
print(homework(a,b))