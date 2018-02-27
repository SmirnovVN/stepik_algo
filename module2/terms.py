def terms(n):
    res = []
    c = 1
    while n:
        if n - c > c:
            n -= c
            res.append(c)
        else:
            res.append(n)
            n = 0
        c += 1
    return res


def main():
    n = int(input())
    res = terms(n)
    print(len(res))
    print(' '.join(str(x) for x in res))


if __name__ == "__main__":
    main()
