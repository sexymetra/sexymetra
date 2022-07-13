def choose_two(n):
    L = []
    for i in range(n):
        for j in range(n):
            a = (i,j)
            if len(set(a)) ==2:
                L.append(set(a))
    M = []
    for k in L:
        if not (k in M):
            M.append(k)
    return M

cases_3 = choose_two( 3 )
print('All cases to choose two out of 3:\n', cases_3 )

cases_4 = choose_two( 4 )
print('All cases to choose two out of 4:\n', cases_4 )

cases_5 = choose_two( 5 )
print('All cases to choose two out of 5:\n', cases_5 )