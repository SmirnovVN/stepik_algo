def cover(lst):
    lst = sorted(lst, key=lambda x: x[1])
    res = []
    while lst:
        d = lst[0][1]
        while lst and lst[0][0] <= d:
            del lst[0]
        res.append(d)
    return res


def main():
    n = int(input())
    o = []
    for i in range(n):
        o.append(list(map(int, input().split())))
    res = cover(o)
    print(len(res))
    print(' '.join(str(x) for x in res))


if __name__ == "__main__":
    main()
