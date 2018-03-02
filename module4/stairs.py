def stairs(a):
    d = [0, a[0]]
    for i in range(1, len(a)):
        d.append(max(d[i-1], d[i]) + a[i])

    return d[len(a)]


def main():
    _ = input()
    a = list(map(int, input().split()))
    print(stairs(a))


if __name__ == "__main__":
    main()
