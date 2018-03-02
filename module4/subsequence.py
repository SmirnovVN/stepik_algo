def lis(a):
    d = [1]*len(a)
    for i in range(len(a)):
        for j in range(i):
            if (a[i] % a[j]) == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(lis(a))


if __name__ == "__main__":
    main()
