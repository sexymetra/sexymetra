import copy
import math
def Inner2D(v, w):
    return v[0]*w[0]+v[1]*w[1]

def radian(p1,p2,p3):
    x1, y1 = p2[0]-p1[0], p2[1]-p1[1]
    x2, y2 = p3[0]-p2[0], p3[1]-p2[1]
    l1, ab_l1 = (x1, y1), math.sqrt(x1**2+y1**2)
    l2, ab_l2 = (x2, y2), math.sqrt(x2**2+y2**2)
    rad = Inner2D(l1,l2)/(ab_l1*ab_l2)
    result = math.acos(rad)
    return result

def Side2D(a,b,S): #직선 ab는 S안에 점들을 한곳에 모는 직선들의 집합에 속하나?
    P = copy.deepcopy(S) #S로 쓰니까 밖이랑 헷갈려서 바꿈
    p_new = min(P) #처음 값
    p_old = p_new[0],p_new[1]-1 #반드시 포함되는 값, x가 최소인 애들중에 y가 최소
    L=[] #점을 한쪽으로 모는 직선들의 집합
    two_point =set({P[a],P[b]}) #들어가있는지 판정해야하는 두 점
    O_p = copy.deepcopy(p_new) #처음 시작 점
    P.remove(p_new)
    while 1: 
        rad_D = {} #각도:좌표
        for i in P:
            rad_D[radian(p_old, p_new, i)] = i
        p_old = copy.deepcopy(p_new) #저번 값
        p_new = rad_D[min(list(rad_D.keys()))] #새로운 값
        line = p_new,p_old
        L.append(set(line))
        P.remove(p_new)
        if (not O_p in P) and len(L) != 1: #한 번 이상 반복된 뒤에 처음 값을 추가해야함
            P.append(O_p)
        if p_new == O_p: #새로운 값이 처음 값과 같아져야 모든 것을 다 찾은 것
            break
    return two_point in L

S = [(0.5, 0.5), (0,-0.5), (1,1), (0,1), (-1,0), (0,-1)]
print( 'S = ', S )
print( 'S lies in the one side of '+str([S[0],S[1]])+'?', Side2D( 0, 1, S ) )
print( 'S lies in the one side of '+str([S[2],S[3]])+'?', Side2D( 2, 3, S ) )
print( 'S lies in the one side of '+str([S[4],S[5]])+'?', Side2D( 4, 5, S ) )