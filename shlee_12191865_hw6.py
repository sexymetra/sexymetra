import random
Name = 'destiny.py'
D = {}
O = []
T = []
with open(Name,'r') as RL:
    while True:
        line = RL.readline()
        if not line:
            break
        if line[0] == '#':
            pass
        else:
            A = line.split() #띄어쓰기 다 없애서 리스트로 만들기
            if len(A) ==3: #원소가 3개 인 것들은 첫째 원소 둘째 원소 셋째까지
                T.append(A)#이 원소 3개 리스트를 하나로 묶음
            elif len(A) ==1:
                O.append(A[0])
# T에는 [~에서, ~어디로, 확률] 의 리스트
first_d = 'family'
N = 5000
for i in range(N):
    if not D.get(first_d,0):
        D[first_d] = 1
    else:
        D[first_d] += 1
    #지금까지 나온 횟수 세기
    nexts = []
    rates = []
    for j in T:             #first와 맞는지 확인하고 맞으면 뒤의 두개 저장
        if j[0] == first_d:
            nexts.append(j[1])
            rates.append(float(j[2]))
    
    C = random.random()
    cut = 0.0
    cut_line = [0]
    for m in range(len(rates)):
        cut = cut + rates[m]
        cut_line.append(cut)
        for n in range(len(cut_line)-1):
            if cut_line[n] < C < cut_line[n+1]:
                first_d = nexts[n]
                    
            
        


Section = ['money', 'love', 'health', 'success', 'respect', 'family']
print('+----------+------------+')
print('|'+f'{"state":^10}'+'|'+f'{"destiney":^12}'+'|')
print('+----------+------------+')
for i in Section:
    print('|'+f'{i:^10}'+'|'+f'{round(D[i]/N,4):^12}'+'|')
print('+----------+------------+')