def dogs_and_cats():
    N, D, C, M = map(int, input().strip().split())
    S = input().strip()

    for k in S:
        if k == 'D':
            if D == 0 or C < 0:
                return "NO"
            D -= 1
            C += M
        else:
            C -= 1
    return "YES"

for case in range(int(input())):
    print ('Case #%d: %s' % (case+1, dogs_and_cats()))