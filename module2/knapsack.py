def rob(w, l):
    l = sorted(l, key=lambda x: x[0]/x[1], reverse=True)
    res = 0.0
    while w and l:
        if l[0][1] <= w:
            res += l[0][0]
            w -= l[0][1]
        else:
            res += l[0][0] * w / l[0][1]
            w = 0
        del l[0]
    return res


n, w = map(int, input().split())
o = []
for i in range(n):
    o.append(list(map(int, input().split())))
print(rob(w, o))
