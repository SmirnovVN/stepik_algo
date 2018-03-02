def calc(n):
    res = [n]
    d = [[float("Inf"), None]] * (n + 1)
    d[1] = [0, lambda x: x]
    operations = [lambda x: x // 3 if (x % 3) == 0 else 0, lambda x: x // 2 if (x % 2) == 0 else 0, lambda x: x - 1]
    for i in range(2, n + 1):
        for op in operations:
            if d[op(i)][0] + 1 < d[i][0]:
                d[i] = [d[op(i)][0] + 1, op]

    for i in range(d[n][0]):
        res.insert(0, d[res[0]][1](res[0]))
    return res


def main():
    n = int(input())
    res = calc(n)
    print(len(res) - 1)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
