import random
Name = input('Lotto Lucky Data = ')
D = {}
with open(Name,'r') as RL:
    RL.readline()
    while True:
        line = RL.readline()
        if not line:
            break
        a,b = map(int,line.split(','))
        D[a] = b
L = [f'{i},'*D[i] for i in D.keys()]


L = ','.join(L)[:-1]
L = L.replace("'',",'')
L = L.replace(",,", ',')
L = L.split(",")

result = []
while len(result)<6:
    C = int(random.choice(L))
    if not C in result:
        result.append(C)
result = str(result).rstrip("]").lstrip("[")
print("Good-Luck Lotto numbers ="+"{"+ str(result)+"}")