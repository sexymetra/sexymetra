def Print_Dict(dct,comment):
    L = [str(i) for i in dct.keys()]
    K = [str(i) for i in dct.values()]
    D = dict(zip(L,K))
    l = len(max(L, key = len))
    k = len(max(K, key = len))
    print('+' + '-'*l + '-' + '-'*k + '+')
    print('|' + comment.center(l+1+k)+'|')
    print('+' + '-'*l + '+' + '-'*k + '+')
    print('|' + 'key'.center(l) + '|' + 'value'.center(k) + '|')
    print('+' + '-'*l + '+' + '-'*k + '+')
    L.sort()
    for i in L:
        print('|' + i.center(l) + '|' + D[i].rjust(k) + '|')
    print('+' + '-'*l + '+' + '-'*k + '+')
def Print_dict(dct,comment):
    L = [str(i) for i in dct.keys()]
    K = [str(i) for i in dct.values()]
    D = dict(zip(L,K))
    l = len(max(L, key = len))
    k = len(max(K, key = len))
    print('+' + '-'*l + '-' + '-'*k + '+')
    print('|' + comment.center(l+1+k)+'|')
    print('+' + '-'*l + '+' + '-'*k + '+')
    print('|' + 'key'.center(l) + '|' + 'value'.center(k) + '|')
    print('+' + '-'*l + '+' + '-'*k + '+')
    L.sort()
    for i in L:
        print('|' + i.center(l) + '|' + D[i].rjust(k) + '|')
    print('+' + '-'*l + '+' + '-'*k + '+')


d1 = { 'Gildong Hong':34, 'pi':3.14, (1,5):100, 1:'who are you?'}
Print_Dict( d1, 'dictionary 1' )

d2 = { 'hello':10, 'a':100, 'One':1, 555:'five five five'}
Print_Dict( d2, 'dictionary 2' )