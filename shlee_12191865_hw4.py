a = open('input.dat','r')
a = a.read()
a = a.replace(".","")
a = a.replace(",","")
a = a.replace("\n"," ").lower()
L = sorted(a.split())
dic = {}
for i in L:
  if dic.get(i):
    dic[i] += 1
  if not dic.get(i):
    dic[i] = 1 
print("+"+'-'*26+"+")
c= 'count'
w = 'word'
print(f"l{w:^16} -> {c:>6}l")
print("+"+'-'*26+"+")
for i in dic.keys():
  a = "["+ i + "]"
  print(f"l{a:>16} -> {dic[i]:>6}l")
print("+"+'-'*26+"+")