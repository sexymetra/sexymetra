A = int(input())
B = int(input())
C = int(input())
D = A*B*C
num = {}
for i in str(D):
  if num.get(i,False):
    num[i] += 1
  else:
    num[i] = 1
L = [str(i) for i in range(10)]
for i in L:
  if num.get(i,False):
    print(num[i])
  else:
    print(0)