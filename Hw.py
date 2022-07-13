import random
D = {}
with open('Lotto_Lucky_Update.py','r') as RL:
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
    C = random.choice(L)
    if not C in result:
        L.append(C)
print(result)