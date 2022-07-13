def inner (x,y):
    sum = 0
    for i in range(len(x)):
        sum += x[i]*y[i]
    return sum
def rot90_2D (v):
    return [-v[1],v[0]]
print('[1,2,3] \u2022 [1,1,1] =', inner( [1,2,3], [1,1,1]))
print('Rotating [1,2] by 90 degree = ', rot90_2D([1,2]))